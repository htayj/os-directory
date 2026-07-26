"use strict";

const columns = [
  { key: "title", label: "Operating system", visible: true, value: row => row.title },
  { key: "editors", label: "Text editors", visible: true, value: row => row.editors.map(x => x.name).join("; ") },
  { key: "relationships", label: "Relationship", visible: true, value: row => row.editors.map(x => x.relationship).join("; ") },
  { key: "evidence", label: "Evidence", visible: true, value: row => row.editors.map(x => x.assertion_status).join("; ") || row.editor_disposition },
  { key: "country", label: "Origin", visible: true, value: row => row.country.join("; ") },
  { key: "purpose", label: "Purpose", visible: true, value: row => row.purpose.join("; ") },
  { key: "first_release", label: "First release", visible: true, value: row => row.first_release },
  { key: "last_updated", label: "Last updated", visible: false, value: row => row.last_updated || row.latest_release },
  { key: "license", label: "License", visible: true, value: row => row.license.join("; ") },
  { key: "programming_language", label: "Language", visible: true, value: row => row.programming_language.join("; ") },
  { key: "gui", label: "Interface", visible: true, value: row => row.gui.join("; ") },
  { key: "platform", label: "Platform", visible: false, value: row => row.platform.join("; ") },
  { key: "kernel", label: "Kernel", visible: true, value: row => row.kernel.join("; ") },
  { key: "development_status", label: "Development", visible: false, value: row => row.development_status },
];

const facets = [
  { key: "editor_availability", label: "Editor coverage", values: row => [row.editor_disposition] },
  { key: "editor", label: "Editor", values: row => row.editors.map(x => x.name) },
  { key: "relationship", label: "Relationship", values: row => row.editors.map(x => x.relationship) },
  { key: "assertion_status", label: "Evidence status", values: row => row.editors.map(x => x.assertion_status) },
  { key: "country", label: "Country / origin", values: row => row.country },
  { key: "purpose", label: "Purpose", values: row => row.purpose },
  { key: "gui", label: "Interface", values: row => row.gui },
  { key: "kernel", label: "Kernel", values: row => row.kernel },
];

const state = {
  rows: [],
  filtered: [],
  query: "",
  filters: Object.fromEntries(facets.map(f => [f.key, ""])),
  sorts: [{ key: "title", direction: "asc" }],
  page: 1,
  pageSize: 50,
};

const el = id => document.getElementById(id);
const fold = value => String(value ?? "").normalize("NFKD").toLocaleLowerCase();
const escapeHtml = value => String(value ?? "").replace(/[&<>"']/g, char => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;",
})[char]);
const label = value => String(value || "unknown").replaceAll("-", " ");

function rowText(row) {
  return fold([
    row.title, row.description, row.development_status, row.catalog_level,
    ...row.country, ...row.purpose, ...row.programming_language, ...row.license,
    row.first_release, row.latest_release, row.last_updated, ...row.gui,
    ...row.platform, ...row.kernel,
    ...row.editors.flatMap(editor => Object.values(editor)),
  ].join(" "));
}

function parseUrl() {
  const params = new URLSearchParams(location.search);
  state.query = params.get("q") || "";
  el("search").value = state.query;
  facets.forEach(facet => state.filters[facet.key] = params.get(facet.key) || "");
  const sort = params.get("sort");
  if (sort) {
    state.sorts = sort.split(",").map(item => {
      const [key, direction] = item.split(":");
      return columns.some(column => column.key === key) && ["asc", "desc"].includes(direction)
        ? { key, direction } : null;
    }).filter(Boolean);
  }
  const size = params.get("rows");
  if (["25", "50", "100", "all"].includes(size)) {
    state.pageSize = size === "all" ? "all" : Number(size);
    el("page-size").value = size;
  }
}

function updateUrl() {
  const params = new URLSearchParams();
  if (state.query) params.set("q", state.query);
  facets.forEach(facet => {
    if (state.filters[facet.key]) params.set(facet.key, state.filters[facet.key]);
  });
  if (!(state.sorts.length === 1 && state.sorts[0].key === "title" && state.sorts[0].direction === "asc")) {
    params.set("sort", state.sorts.map(sort => `${sort.key}:${sort.direction}`).join(","));
  }
  if (state.pageSize !== 50) params.set("rows", state.pageSize);
  history.replaceState(null, "", `${location.pathname}${params.size ? `?${params}` : ""}`);
}

function facetOptions(facet) {
  return [...new Set(state.rows.flatMap(facet.values).filter(Boolean))]
    .sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true }));
}

function buildFilters() {
  el("filter-panel").innerHTML = facets.map(facet => {
    const options = facetOptions(facet).map(value =>
      `<option value="${escapeHtml(value)}">${escapeHtml(label(value))}</option>`
    ).join("");
    return `<label>${escapeHtml(facet.label)}
      <select data-filter="${facet.key}">
        <option value="">All</option>${options}
      </select>
    </label>`;
  }).join("");
  document.querySelectorAll("[data-filter]").forEach(select => {
    select.value = state.filters[select.dataset.filter];
    select.addEventListener("change", event => {
      state.filters[event.target.dataset.filter] = event.target.value;
      state.page = 1;
      render();
    });
  });
}

function buildColumns() {
  el("column-panel").innerHTML = columns.map(column =>
    `<label><input type="checkbox" data-column="${column.key}" ${column.visible ? "checked" : ""}> ${escapeHtml(column.label)}</label>`
  ).join("");
  document.querySelectorAll("[data-column]").forEach(input => {
    input.addEventListener("change", event => {
      columns.find(column => column.key === event.target.dataset.column).visible = event.target.checked;
      buildHead();
      renderRows();
    });
  });
}

function buildHead() {
  el("table-head").innerHTML = columns.filter(column => column.visible).map(column => {
    const index = state.sorts.findIndex(sort => sort.key === column.key);
    const mark = index < 0 ? "" : `${state.sorts[index].direction === "asc" ? "↑" : "↓"}${state.sorts.length > 1 ? index + 1 : ""}`;
    const aria = index < 0 ? "none" : state.sorts[index].direction === "asc" ? "ascending" : "descending";
    return `<th scope="col" aria-sort="${aria}">
      <button type="button" data-sort="${column.key}" title="Click to sort; Shift-click for multi-column sort">
        ${escapeHtml(column.label)} <span class="sort-mark">${mark}</span>
      </button>
    </th>`;
  }).join("");
  document.querySelectorAll("[data-sort]").forEach(button => {
    button.addEventListener("click", event => setSort(button.dataset.sort, event.shiftKey));
  });
}

function setSort(key, additive) {
  const current = state.sorts.find(sort => sort.key === key);
  let next;
  if (!current) next = { key, direction: "asc" };
  else if (current.direction === "asc") next = { key, direction: "desc" };
  else next = null;
  state.sorts = additive ? state.sorts.filter(sort => sort.key !== key) : [];
  if (next) state.sorts.push(next);
  state.page = 1;
  render();
}

function applyFilters() {
  const terms = fold(state.query).split(/\s+/).filter(Boolean);
  state.filtered = state.rows.filter(row => {
    const haystack = row._search;
    if (!terms.every(term => haystack.includes(term))) return false;
    return facets.every(facet => {
      const selected = state.filters[facet.key];
      return !selected || facet.values(row).includes(selected);
    });
  });
  if (state.sorts.length) {
    state.filtered.sort((a, b) => {
      for (const sort of state.sorts) {
        const column = columns.find(item => item.key === sort.key);
        const result = String(column.value(a)).localeCompare(String(column.value(b)), undefined, { numeric: true, sensitivity: "base" });
        if (result) return sort.direction === "asc" ? result : -result;
      }
      return a.title.localeCompare(b.title);
    });
  }
}

function chips(values) {
  if (!values.length) return `<span class="muted">Unknown</span>`;
  return `<div class="cell-list">${values.map(value => `<span class="chip">${escapeHtml(value)}</span>`).join("")}</div>`;
}

function editorCell(row) {
  if (!row.editors.length) return `<span class="muted">No evidence found</span>`;
  return `<div class="editor-stack">${row.editors.map(editor => `
    <div class="editor ${escapeHtml(editor.assertion_status)}">
      <a href="${escapeHtml(editor.source)}" rel="noreferrer">${escapeHtml(editor.name)} <span aria-hidden="true">↗</span></a>
      <span class="editor-meta">${escapeHtml(label(editor.relationship))}${editor.interface_style ? ` · ${escapeHtml(label(editor.interface_style))}` : ""}</span>
    </div>`).join("")}</div>`;
}

function cell(column, row) {
  if (column.key === "title") return `<td class="system-cell"><a href="${escapeHtml(row.record_url)}">${escapeHtml(row.title)}</a><small>${escapeHtml(row.description)}</small></td>`;
  if (column.key === "editors") return `<td>${editorCell(row)}</td>`;
  if (column.key === "relationships") return `<td>${chips([...new Set(row.editors.map(x => label(x.relationship)))])}</td>`;
  if (column.key === "evidence") {
    if (!row.editors.length) return `<td><span class="status">${escapeHtml(label(row.editor_disposition))}</span></td>`;
    return `<td>${[...new Set(row.editors.map(x => x.assertion_status))].map(value => `<span class="status ${escapeHtml(value)}">${escapeHtml(label(value))}</span>`).join("<br>")}</td>`;
  }
  const value = column.value(row);
  const values = Array.isArray(row[column.key]) ? row[column.key] : value ? [value] : [];
  return `<td>${chips(values)}</td>`;
}

function renderRows() {
  const visible = columns.filter(column => column.visible);
  const size = state.pageSize === "all" ? Math.max(state.filtered.length, 1) : state.pageSize;
  const pages = Math.max(1, Math.ceil(state.filtered.length / size));
  state.page = Math.min(state.page, pages);
  const start = (state.page - 1) * size;
  const rows = state.filtered.slice(start, start + size);
  el("table-body").innerHTML = rows.map(row =>
    `<tr>${visible.map(column => cell(column, row)).join("")}</tr>`
  ).join("");
  el("empty").hidden = state.filtered.length !== 0;
  el("table-body").closest("table").hidden = state.filtered.length === 0;
  el("previous").disabled = state.page <= 1;
  el("next").disabled = state.page >= pages;
  el("page-status").textContent = `Page ${state.page} of ${pages}`;
  el("result-count").innerHTML = `<strong>${state.filtered.length.toLocaleString()}</strong> of ${state.rows.length.toLocaleString()} systems`;
}

function render() {
  applyFilters();
  buildHead();
  renderRows();
  const active = facets.filter(facet => state.filters[facet.key]).length;
  el("filter-count").textContent = active;
  updateUrl();
}

function csvValue(value) {
  return `"${String(value ?? "").replaceAll('"', '""')}"`;
}

function exportCsv() {
  const exportColumns = columns.filter(column => column.visible);
  const lines = [
    exportColumns.map(column => csvValue(column.label)).join(","),
    ...state.filtered.map(row => exportColumns.map(column => csvValue(column.value(row))).join(",")),
  ];
  const blob = new Blob([`\uFEFF${lines.join("\n")}\n`], { type: "text/csv;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "operating-systems-and-text-editors.csv";
  link.click();
  URL.revokeObjectURL(link.href);
}

function togglePanel(button, panel) {
  const open = panel.hidden;
  panel.hidden = !open;
  button.setAttribute("aria-expanded", String(open));
}

async function init() {
  try {
    const response = await fetch("data.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    state.rows = data.systems.map(row => ({ ...row, _search: rowText(row) }));
    el("stat-systems").textContent = data.stats.systems.toLocaleString();
    el("stat-editors").textContent = data.stats.unique_editors.toLocaleString();
    el("stat-associations").textContent = data.stats.associations.toLocaleString();
    el("stat-documented").textContent = data.stats.documented_associations.toLocaleString();
    el("as-of").textContent = `Catalog snapshot: ${data.as_of || "undated"}.`;
    parseUrl();
    buildFilters();
    buildColumns();
    render();
  } catch (error) {
    el("result-count").textContent = `Could not load catalog data: ${error.message}`;
  }
}

el("search").addEventListener("input", event => {
  state.query = event.target.value.trim();
  state.page = 1;
  render();
});
el("page-size").addEventListener("change", event => {
  state.pageSize = event.target.value === "all" ? "all" : Number(event.target.value);
  state.page = 1;
  render();
});
el("previous").addEventListener("click", () => { state.page -= 1; renderRows(); });
el("next").addEventListener("click", () => { state.page += 1; renderRows(); });
el("export").addEventListener("click", exportCsv);
el("reset").addEventListener("click", () => {
  state.query = "";
  el("search").value = "";
  facets.forEach(facet => {
    state.filters[facet.key] = "";
    const select = document.querySelector(`[data-filter="${facet.key}"]`);
    if (select) select.value = "";
  });
  state.sorts = [{ key: "title", direction: "asc" }];
  state.page = 1;
  render();
});
el("filters-toggle").addEventListener("click", () => togglePanel(el("filters-toggle"), el("filter-panel")));
el("columns-toggle").addEventListener("click", () => togglePanel(el("columns-toggle"), el("column-panel")));
document.addEventListener("keydown", event => {
  if (event.key === "/" && !["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement.tagName)) {
    event.preventDefault();
    el("search").focus();
  }
});

init();

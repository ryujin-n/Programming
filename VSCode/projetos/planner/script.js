const $ = (s) => document.querySelector(s);
const BRL = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});
const money = (n) => BRL.format(n);
const esc = (s) =>
  String(s == null ? "" : s).replace(
    /[&<>"]/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c],
  );
const STAT = [
  "Quero comprar",
  "Pesquisando",
  "Esperando promoção",
  "Comprado",
  "Esgotado",
];
const RANK = { Alta: 1, Média: 2, Baixa: 3 };
const KEY = "compras_futuras_v1";
const SEED = [
  [
    'Monitor Gamer LG UltraGear 34GX90SA 34" OLED WQHD 240Hz',
    "Periféricos",
    "Pichau",
    "Quero comprar",
    6599.99,
    12,
    647.06,
  ],
  [
    "SSD WD Black SN8100 4TB M.2 NVMe",
    "Armazenamento",
    "Pichau",
    "Quero comprar",
    7759.99,
    12,
    760.78,
  ],
  [
    "Processador AMD Ryzen 9 9950X3D 16-Core 4.3GHz",
    "Hardware PC",
    "Pichau",
    "Quero comprar",
    4299.99,
    12,
    421.57,
  ],
  [
    "Placa de Vídeo ASUS ROG Astral RTX 5080 OC 16GB",
    "Hardware PC",
    "Pichau",
    "Esgotado",
    null,
    null,
    null,
  ],
  [
    "Leitor Externo Dock Clonador HD/SATA SSD USB",
    "Armazenamento",
    "Mercado Livre",
    "Quero comprar",
    169.11,
    12,
    16.71,
  ],
  [
    "Estojo/Case p/ Disco Rígido Externo Ugreen",
    "Acessórios",
    "Mercado Livre",
    "Quero comprar",
    72.9,
    3,
    24.3,
  ],
  [
    "Celular Samsung Galaxy S26 5G 256GB 12GB RAM",
    "Celular",
    "Mercado Livre",
    "Quero comprar",
    4798,
    10,
    533.2,
  ],
  [
    "Power Bank Baseus Bipow2 Pro 30000mAh 22,5W",
    "Acessórios",
    "Mercado Livre",
    "Quero comprar",
    289.5,
    1,
    299.5,
  ],
];
let S = {
  items: [],
  lojas: ["Mercado Livre", "Pichau", "WAZ"],
  cats: [
    "Hardware PC",
    "Armazenamento",
    "Periféricos",
    "Celular",
    "Acessórios",
    "Games",
    "Casa",
    "Estudos",
    "Outros",
  ],
  meta: "",
  f: { s: "pend", l: "", o: "prio", q: "" },
  edit: null,
};
function uid() {
  return "i" + Date.now().toString(36) + Math.random().toString(36).slice(2, 5);
}
function load() {
  let ok = false;
  try {
    const r = localStorage.getItem(KEY);
    if (r) {
      const d = JSON.parse(r);
      S.items = d.items || [];
      S.lojas = d.lojas || S.lojas;
      S.cats = d.cats || S.cats;
      S.meta = d.meta || "";
      ok = true;
    }
  } catch (e) {}
  if (!ok)
    S.items = SEED.map((x, i) => ({
      id: uid(),
      nome: x[0],
      link: "",
      cat: x[1],
      loja: x[2],
      prio: "",
      qtd: 1,
      preco: x[4],
      pagto: "",
      parc: x[5],
      vparc: x[6],
      data: "",
      obs: "",
      status: x[3],
      criado: Date.now() + i,
    }));
}
function save() {
  try {
    localStorage.setItem(
      KEY,
      JSON.stringify({
        items: S.items,
        lojas: S.lojas,
        cats: S.cats,
        meta: S.meta,
      }),
    );
  } catch (e) {}
}
function parseBR(s) {
  s = String(s || "").replace(/R\$|\s/gi, "");
  if (!s) return null;
  if (s.includes(",")) {
    s = s.replace(/\./g, "").replace(",", ".");
  } else if (s.includes(".")) {
    const p = s.split(".");
    if (p.length > 2 || p[p.length - 1].length > 2) s = s.replace(/\./g, "");
  }
  return /^\d+(\.\d+)?$/.test(s) ? parseFloat(s) : NaN;
}
const tot = (i) => (i.preco != null ? i.preco * (i.qtd || 1) : 0);
const pend = (i) => i.status !== "Comprado";

/* ---- link: loja, nome e categoria a partir do endereço ---- */
const KNOWN = {
  mercadolivre: "Mercado Livre",
  mercadolibre: "Mercado Livre",
  pichau: "Pichau",
  wazshop: "WAZ",
  waz: "WAZ",
  kabum: "KaBuM",
  terabyteshop: "Terabyte",
  amazon: "Amazon",
  magazineluiza: "Magalu",
  magalu: "Magalu",
  shopee: "Shopee",
  aliexpress: "AliExpress",
};
const UP = new Set([
  "ssd",
  "hd",
  "hdd",
  "usb",
  "led",
  "oled",
  "rgb",
  "gpu",
  "cpu",
  "ram",
  "nvme",
  "amd",
  "lg",
  "wd",
  "tv",
  "pc",
  "hdmi",
  "wifi",
]);
const LOW = new Set([
  "de",
  "da",
  "do",
  "para",
  "com",
  "e",
  "p",
  "em",
  "a",
  "o",
]);
function storeFromUrl(u) {
  try {
    const h = new URL(u).hostname.replace(/^www\./, "");
    for (const k in KNOWN) if (h.includes(k)) return KNOWN[k];
    const n = h.split(".")[0];
    return n.charAt(0).toUpperCase() + n.slice(1);
  } catch (e) {
    return "";
  }
}
function nameFromUrl(u) {
  try {
    const url = new URL(u);
    let segs = decodeURIComponent(url.pathname)
      .split("/")
      .filter((s) => s.length > 8 && !/^(MLB\d+)$/i.test(s));
    if (!segs.length) return "";
    segs.sort(
      (a, b) => (b.match(/-/g) || []).length - (a.match(/-/g) || []).length,
    );
    let s = segs[0]
      .replace(/\.(html?|php)$/i, "")
      .replace(/^MLB-?\d+-/i, "")
      .replace(/-?_JM.*$/i, "")
      .replace(/[-_]+/g, " ")
      .trim();
    if (s.split(" ").length < 2) return "";
    return s
      .split(" ")
      .map((w, i) => {
        const l = w.toLowerCase();
        if (UP.has(l) || /\d/.test(l)) return w.toUpperCase();
        if (i && LOW.has(l)) return l;
        return w.charAt(0).toUpperCase() + w.slice(1);
      })
      .join(" ");
  } catch (e) {
    return "";
  }
}
const CATS = [
  [
    "Acessórios",
    [
      "estojo",
      "power bank",
      "powerbank",
      "carregador",
      "cabo ",
      "capa ",
      "película",
      "suporte",
      "adaptador",
    ],
  ],
  [
    "Celular",
    [
      "celular",
      "smartphone",
      "iphone",
      "galaxy s",
      "galaxy a",
      "redmi",
      "moto g",
    ],
  ],
  [
    "Periféricos",
    ["monitor", "teclado", "mouse", "headset", "fone ", "webcam", "microfone"],
  ],
  [
    "Armazenamento",
    [
      "ssd",
      "hdd",
      "hd externo",
      "nvme",
      "pendrive",
      "dock",
      "clonador",
      "disco",
    ],
  ],
  ["Games", ["playstation", "xbox", "nintendo", "console", "controle"]],
  [
    "Hardware PC",
    [
      "processador",
      "placa de vídeo",
      "placa de video",
      "memória ram",
      "placa-mãe",
      "placa mãe",
      "fonte ",
      "gabinete",
      "cooler",
      "rtx",
      "radeon",
      "ryzen",
      "geforce",
      "intel core",
    ],
  ],
];
function catFromName(n) {
  n = n.toLowerCase() + " ";
  for (const [c, ks] of CATS) if (ks.some((k) => n.includes(k))) return c;
  return "";
}

/* ---- formulário ---- */
const F = (id) => $("#" + id);
function fillAuto(el, v) {
  if (v && (!el.value || el.dataset.auto === "1")) {
    el.value = v;
    el.dataset.auto = "1";
  }
}
["f_nome", "f_loja", "f_cat"].forEach((id) =>
  F(id).addEventListener("input", () => {
    F(id).dataset.auto = "";
  }),
);
F("f_link").addEventListener("input", () => {
  const u = F("f_link").value.trim();
  if (!/^https?:\/\/\S+/i.test(u)) {
    F("lmsg").textContent = "";
    return;
  }
  fillAuto(F("f_loja"), storeFromUrl(u));
  fillAuto(F("f_nome"), nameFromUrl(u));
  fillAuto(F("f_cat"), catFromName(F("f_nome").value));
  F("lmsg").textContent =
    "Loja, nome e categoria sugeridos pelo endereço. O preço esta página não consegue buscar: digite abaixo.";
});
function resetForm() {
  F("form").reset();
  ["f_nome", "f_loja", "f_cat"].forEach((i) => (F(i).dataset.auto = ""));
  S.edit = null;
  F("ftit").textContent = "Novo item";
  F("fsave").textContent = "Adicionar à lista";
  F("fcancel").hidden = true;
  F("lmsg").textContent = "";
}
F("fcancel").onclick = () => {
  resetForm();
  F("fmsg").textContent = "";
};
F("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const bad = (m) => {
    F("fmsg").textContent = m;
    F("fmsg").style.color = "var(--bad)";
  };
  const nome = F("f_nome").value.trim();
  if (!nome) return bad("Informe o nome do produto.");
  const preco = parseBR(F("f_preco").value),
    vp = parseBR(F("f_vparc").value);
  if (Number.isNaN(preco))
    return bad("Preço à vista inválido. Exemplo: 4299,99");
  if (Number.isNaN(vp))
    return bad("Valor da parcela inválido. Exemplo: 647,06");
  const loja = F("f_loja").value.trim(),
    cat = F("f_cat").value.trim();
  const base = {
    nome,
    link: F("f_link").value.trim(),
    cat,
    loja,
    prio: F("f_prio").value,
    qtd: Math.max(1, parseInt(F("f_qtd").value) || 1),
    preco,
    pagto: F("f_pagto").value,
    parc: parseInt(F("f_parc").value) || null,
    vparc: vp,
    data: F("f_data").value,
    obs: F("f_obs").value.trim(),
  };
  let extra = "";
  if (loja && !S.lojas.some((x) => x.toLowerCase() === loja.toLowerCase())) {
    S.lojas.push(loja);
    extra = " Loja " + loja + " cadastrada.";
  }
  if (cat && !S.cats.some((x) => x.toLowerCase() === cat.toLowerCase()))
    S.cats.push(cat);
  if (S.edit) {
    Object.assign(
      S.items.find((i) => i.id === S.edit),
      base,
    );
  } else
    S.items.push(
      Object.assign(base, {
        id: uid(),
        status: "Quero comprar",
        criado: Date.now(),
      }),
    );
  const ed = !!S.edit;
  resetForm();
  save();
  render();
  F("fmsg").style.color = "var(--mut)";
  F("fmsg").textContent =
    (ed ? "Alterações salvas." : "Item adicionado.") + extra;
});
function editItem(id) {
  const i = S.items.find((x) => x.id === id);
  if (!i) return;
  S.edit = id;
  const set = (k, v) => {
    F(k).value = v == null ? "" : v;
    F(k).dataset.auto = "";
  };
  set("f_nome", i.nome);
  set("f_link", i.link);
  set("f_loja", i.loja);
  set("f_cat", i.cat);
  set("f_prio", i.prio || "Média");
  set("f_qtd", i.qtd || 1);
  set("f_preco", i.preco == null ? "" : String(i.preco).replace(".", ","));
  set("f_pagto", i.pagto);
  set("f_parc", i.parc);
  set("f_vparc", i.vparc == null ? "" : String(i.vparc).replace(".", ","));
  set("f_data", i.data);
  set("f_obs", i.obs);
  F("ftit").textContent = "Editar item";
  F("fsave").textContent = "Salvar alterações";
  F("fcancel").hidden = false;
  F("lmsg").textContent = "";
  F("f_nome").scrollIntoView({ block: "center" });
  F("f_nome").focus();
}

/* ---- lista ---- */
function opts(el, arr, first) {
  const v = el.value;
  el.innerHTML = first
    .concat(arr.map((x) => [x, x]))
    .map(([a, b]) => `<option value="${esc(a)}">${esc(b)}</option>`)
    .join("");
  el.value = v;
}
function render() {
  F("dl_loja").innerHTML = S.lojas
    .map((x) => `<option value="${esc(x)}">`)
    .join("");
  F("dl_cat").innerHTML = S.cats
    .map((x) => `<option value="${esc(x)}">`)
    .join("");
  opts(F("fs"), STAT, [
    ["pend", "Pendentes"],
    ["all", "Todos os status"],
  ]);
  if (!F("fs").value) F("fs").value = S.f.s;
  opts(
    F("fl"),
    [
      ...new Set(
        S.items
          .map((i) => i.loja)
          .filter(Boolean)
          .concat(S.lojas),
      ),
    ],
    [["", "Todas as lojas"]],
  );
  const P = S.items.filter(pend);
  F("kPend").textContent = money(P.reduce((a, i) => a + tot(i), 0));
  F("kBuy").textContent = money(
    S.items.filter((i) => !pend(i)).reduce((a, i) => a + tot(i), 0),
  );
  F("kQtd").textContent = P.length;
  F("kEco").textContent = money(
    P.reduce(
      (a, i) =>
        a +
        (i.preco != null && i.parc && i.vparc
          ? Math.max(0, (i.parc * i.vparc - i.preco) * (i.qtd || 1))
          : 0),
      0,
    ),
  );
  const m = parseBR(F("meta").value),
    t = P.reduce((a, i) => a + tot(i), 0);
  F("meses").textContent =
    m > 0 ? `≈ ${Math.ceil(t / m)} meses para juntar o pendente` : "";
  const by = {};
  P.forEach((i) => {
    const k = i.loja || "Sem loja";
    by[k] = by[k] || { n: 0, t: 0 };
    by[k].n++;
    by[k].t += tot(i);
  });
  F("stores").innerHTML = Object.entries(by)
    .sort((a, b) => b[1].t - a[1].t)
    .map(
      ([k, v]) =>
        `<div class="chip">${esc(k)}<b>${money(v.t)}</b>${v.n} ite${v.n > 1 ? "ns" : "m"}</div>`,
    )
    .join("");
  const f = S.f,
    q = f.q.toLowerCase();
  let L = S.items.filter(
    (i) =>
      (f.s === "all" || (f.s === "pend" ? pend(i) : i.status === f.s)) &&
      (!f.l || i.loja === f.l) &&
      (!q ||
        (i.nome + " " + i.loja + " " + i.cat + " " + i.obs)
          .toLowerCase()
          .includes(q)),
  );
  L.sort(
    f.o === "new"
      ? (a, b) => b.criado - a.criado
      : f.o === "price"
        ? (a, b) => tot(b) - tot(a)
        : (a, b) =>
            (RANK[a.prio] || 4) - (RANK[b.prio] || 4) || b.criado - a.criado,
  );
  F("empty").hidden = L.length > 0;
  F("rows").innerHTML = L.map(
    (
      i,
    ) => `<tr class="${pend(i) ? "" : "done"}" data-id="${i.id}"><td><div class="nm">${i.link ? `<a href="${esc(i.link)}" target="_blank" rel="noopener noreferrer">${esc(i.nome)}</a>` : esc(i.nome)}</div><div class="sm">${esc([i.cat, i.pagto, i.data ? "em " + i.data.split("-").reverse().join("/") : ""].filter(Boolean).join(" · "))}</div>${i.obs ? `<div class="sm">${esc(i.obs)}</div>` : ""}</td>
          <td>${esc(i.loja)}</td><td>${i.prio ? `<span class="b ${esc(i.prio)}">${esc(i.prio)}</span>` : ""}</td><td class="num">${i.qtd || 1}</td>
          <td class="num">${i.preco != null ? money(i.preco) : "—"}${i.parc && i.vparc ? `<div class="sm">${i.parc}× ${money(i.vparc)}</div>` : ""}</td><td class="num"><b>${i.preco != null ? money(tot(i)) : "—"}</b></td>
          <td><select data-a="st">${STAT.map((s) => `<option${s === i.status ? " selected" : ""}>${s}</option>`).join("")}</select></td>
          <td class="num"><button class="ic" data-a="buy" title="Marcar como comprado">✓</button> <button class="ic" data-a="ed" title="Editar">✎</button> <button class="ic del" data-a="del" title="Excluir">✕</button></td></tr>`,
  ).join("");
}
F("rows").addEventListener("click", (e) => {
  const b = e.target.closest("button");
  if (!b) return;
  const id = b.closest("tr").dataset.id,
    a = b.dataset.a;
  if (a === "ed") return editItem(id);
  if (a === "buy") {
    const i = S.items.find((x) => x.id === id);
    i.status = "Comprado";
    save();
    return render();
  }
  if (a === "del") {
    if (b.dataset.arm) {
      S.items = S.items.filter((x) => x.id !== id);
      save();
      return render();
    }
    b.dataset.arm = "1";
    b.textContent = "Excluir?";
    setTimeout(() => {
      b.dataset.arm = "";
      b.textContent = "✕";
    }, 3000);
  }
});
F("rows").addEventListener("change", (e) => {
  if (e.target.dataset.a !== "st") return;
  S.items.find((x) => x.id === e.target.closest("tr").dataset.id).status =
    e.target.value;
  save();
  render();
});
F("fs").onchange = () => {
  S.f.s = F("fs").value;
  render();
};
F("fl").onchange = () => {
  S.f.l = F("fl").value;
  render();
};
F("fo").onchange = () => {
  S.f.o = F("fo").value;
  render();
};
F("fq").oninput = () => {
  S.f.q = F("fq").value;
  render();
};
F("meta").oninput = () => {
  S.meta = F("meta").value;
  save();
  render();
};

/* ---- backup ---- */
const csvq = (v) => '"' + String(v == null ? "" : v).replace(/"/g, '""') + '"';
function baixar(nome, tipo, txt) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([txt], { type: tipo }));
  a.download = nome;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    URL.revokeObjectURL(a.href);
    a.remove();
  }, 500);
}
F("xcsv").onclick = () => {
  const h = [
    "Produto",
    "Categoria",
    "Loja",
    "Prioridade",
    "Status",
    "Qtd",
    "Preço à vista",
    "Pagamento",
    "Parcelas",
    "Valor parcela",
    "Total à vista",
    "Data planejada",
    "Link",
    "Observações",
  ];
  const rows = S.items.map((i) => [
    i.nome,
    i.cat,
    i.loja,
    i.prio,
    i.status,
    i.qtd,
    i.preco == null ? "" : String(i.preco).replace(".", ","),
    i.pagto,
    i.parc,
    i.vparc == null ? "" : String(i.vparc).replace(".", ","),
    i.preco == null ? "" : String(tot(i)).replace(".", ","),
    i.data,
    i.link,
    i.obs,
  ]);
  baixar(
    "compras-futuras.csv",
    "text/csv;charset=utf-8",
    "\ufeff" +
      [h]
        .concat(rows)
        .map((r) => r.map(csvq).join(";"))
        .join("\r\n"),
  );
};
F("xjson").onclick = () =>
  baixar(
    "compras-futuras-backup.json",
    "application/json",
    JSON.stringify({
      items: S.items,
      lojas: S.lojas,
      cats: S.cats,
      meta: S.meta,
    }),
  );
F("ijson").onclick = () => F("ifile").click();
F("ifile").onchange = (e) => {
  const f = e.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try {
      const d = JSON.parse(r.result);
      if (!Array.isArray(d.items)) throw 0;
      S.items = d.items;
      S.lojas = d.lojas || S.lojas;
      S.cats = d.cats || S.cats;
      S.meta = d.meta || "";
      F("meta").value = S.meta;
      save();
      render();
    } catch (x) {
      F("fmsg").textContent = "Arquivo de backup inválido.";
    }
  };
  r.readAsText(f);
  e.target.value = "";
};

load();
F("meta").value = S.meta;
render();

// fuc dat shi mann

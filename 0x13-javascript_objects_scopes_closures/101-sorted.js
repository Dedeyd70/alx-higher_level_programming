#!/usr/bin/node
const originalDict = require('./101-data').dict;

const dictEntries = Object.entries(originalDict);
const vals = Object.values(originalDict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in dictEntries) {
    if (dictEntries[k][1] === valsUniq[j]) {
      list.unshift(dictEntries[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);

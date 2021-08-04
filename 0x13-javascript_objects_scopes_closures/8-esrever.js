#!/usr/bin/node

exports.esrever = function (list) {
  const size = (list.length - 1);
  const reverlist = [];
  for (let i = size; i >= 0; --i) {
    reverlist.push(list[i]);
  }
  return (reverlist);
};

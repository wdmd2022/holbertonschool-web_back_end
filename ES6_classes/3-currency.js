export default class Currency {
  constructor(code, name) {
    if (typeof code === 'string') {
      this._code = code;
    }
    if (typeof name === 'string') {
      this._name = name;
    }
  }

  // Stop! Getter time //
  get code() {
    return (this._code);
  }

  get name() {
    return (this._name);
  }

  // game... SET! ...match //
  set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    }
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
  }

  // not mad just have a METHOD //
  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}

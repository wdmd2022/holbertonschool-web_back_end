import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount === 'number') {
      this._amount = amount;
    }
    if (currency instanceof Currency) {
      this._currency = currency;
    }
  }

  // let's get ready to GET some stuff //
  get amount() {
    return (this._amount);
  }

  get currency() {
    return (this._currency);
  }

  // let's SET this class up for success //
  set amount(amount) {
    if (typeof amount === 'number') {
      this._amount = amount;
    }
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      this._currency = currency;
    }
  }

  // Method time //
  displayFullPrice() {
    return (`${this._amount} ${this._currency.displayFullCurrency()}`);
  }

  // Static Method time! (i.e. can only call on class itself) //
  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }
}

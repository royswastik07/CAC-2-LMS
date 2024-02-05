function submitPayment() {
    const cardNumber = document.getElementById('cardNumber').value;
    const expiryDate = document.getElementById('expiryDate').value;
    const cvv = document.getElementById('cvv').value;
    const amount = document.getElementById('amount').value;
  
    if (validateCardNumber(cardNumber) && validateExpiryDate(expiryDate) && validateCVV(cvv) && validateAmount(amount)) {
      displayPaymentMessage('Payment successful! Amount: $', 'success', amount);
    } else {
      displayPaymentMessage('Invalid input or missing fields. Please check and try again.', 'error');
    }
  }
  
  function validateCardNumber(cardNumber) {
    // Remove spaces from the card number for validation
    const strippedCardNumber = cardNumber.replace(/\s/g, '');
  
    // Check if the stripped card number is a 16-digit numeric value
    return /^\d{16}$/.test(strippedCardNumber);
  }
  
  function validateExpiryDate(expiryDate) {
    const isValidFormat = /^\d{2}\/\d{4}$/.test(expiryDate);
  
    if (!isValidFormat) return false;
  
    const [month, year] = expiryDate.split('/');
    const inputDate = new Date(`${year}-${month}-01`);
    const currentDate = new Date();
  
    return inputDate > currentDate;
  }
  
  function validateCVV(cvv) {
    return /^\d{3}$/.test(cvv);
  }
  
  function validateAmount(amount) {
    return validator.isNumeric(amount);
  }
  
  function displayPaymentMessage(message, type = 'success', amount = '') {
    const paymentMessage = document.getElementById('paymentMessage');
    paymentMessage.textContent = message + amount;
    paymentMessage.className = type;
  
    // Clear the message after 5 seconds
    setTimeout(() => {
      paymentMessage.textContent = '';
      paymentMessage.className = '';
    }, 5000);
  }
  
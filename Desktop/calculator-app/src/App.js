import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentOperand, setCurrentOperand] = useState('0');
  const [previousOperand, setPreviousOperand] = useState('');
  const [operation, setOperation] = useState('');
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const [darkMode, setDarkMode] = useState(true);
  const [scientificMode, setScientificMode] = useState(false);
  const [memory, setMemory] = useState(0);
  const [shouldResetDisplay, setShouldResetDisplay] = useState(false);

  // Keyboard support
  useEffect(() => {
    const handleKeyPress = (e) => {
      if (e.key >= '0' && e.key <= '9') {
        handleNumberClick(e.key);
      } else if (e.key === '.') {
        handleDecimalClick();
      } else if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') {
        handleOperatorClick(e.key);
      } else if (e.key === 'Enter' || e.key === '=') {
        e.preventDefault();
        handleEqualsClick();
      } else if (e.key === 'Escape') {
        clear();
      } else if (e.key === 'Backspace') {
        handleDelete();
      } else if (e.key === '%') {
        handlePercentage();
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentOperand, previousOperand, operation]);

  // Handle number button clicks
  const handleNumberClick = (number) => {
    if (shouldResetDisplay) {
      setCurrentOperand(number);
      setShouldResetDisplay(false);
    } else if (currentOperand === '0') {
      setCurrentOperand(number);
    } else {
      setCurrentOperand(currentOperand + number);
    }
  };

  // Handle decimal point
  const handleDecimalClick = () => {
    if (!currentOperand.includes('.')) {
      setCurrentOperand(currentOperand + '.');
    }
  };

  // Handle delete/backspace
  const handleDelete = () => {
    if (currentOperand.length === 1) {
      setCurrentOperand('0');
    } else {
      setCurrentOperand(currentOperand.slice(0, -1));
    }
  };

  // Handle percentage
  const handlePercentage = () => {
    const value = parseFloat(currentOperand);
    if (!isNaN(value)) {
      setCurrentOperand((value / 100).toString());
    }
  };

  // Handle sign change
  const handleSignChange = () => {
    if (currentOperand !== '0') {
      setCurrentOperand((parseFloat(currentOperand) * -1).toString());
    }
  };

  // Handle operator button clicks (+, -, *, /)
  const handleOperatorClick = (operator) => {
    if (currentOperand === '') {
      // If no current operand, just change the operator
      if (previousOperand !== '') {
        setOperation(operator);
      }
      return;
    }
    
    if (previousOperand !== '' && operation !== '') {
      // Chain calculations: calculate the previous operation first
      const prev = parseFloat(previousOperand);
      const current = parseFloat(currentOperand);
      
      if (!isNaN(prev) && !isNaN(current)) {
        let result;
        switch (operation) {
          case '+':
            result = prev + current;
            break;
          case '-':
            result = prev - current;
            break;
          case '*':
            result = prev * current;
            break;
          case '/':
            if (current === 0) {
              alert('Cannot divide by zero!');
              clear();
              return;
            }
            result = prev / current;
            break;
          default:
            return;
        }
        
        const formattedResult = formatResult(result);
        const calculation = `${prev} ${operation} ${current} = ${formattedResult}`;
        setHistory([calculation, ...history.slice(0, 9)]);
        
        // Set up for next operation
        setPreviousOperand(formattedResult.toString());
        setCurrentOperand(formattedResult.toString());
        setOperation(operator);
        setShouldResetDisplay(true);
      }
    } else {
      setOperation(operator);
      setPreviousOperand(currentOperand);
      setCurrentOperand('');
    }
  };

  // Scientific functions
  const handleScientific = (func) => {
    const value = parseFloat(currentOperand);
    if (isNaN(value)) return;

    let result;
    switch (func) {
      case 'sin':
        result = Math.sin(value * Math.PI / 180);
        break;
      case 'cos':
        result = Math.cos(value * Math.PI / 180);
        break;
      case 'tan':
        result = Math.tan(value * Math.PI / 180);
        break;
      case 'sqrt':
        result = Math.sqrt(value);
        break;
      case 'square':
        result = value * value;
        break;
      case 'log':
        result = Math.log10(value);
        break;
      case 'ln':
        result = Math.log(value);
        break;
      case 'exp':
        result = Math.exp(value);
        break;
      case 'pi':
        result = Math.PI;
        break;
      case 'e':
        result = Math.E;
        break;
      default:
        return;
    }

    const formattedResult = formatResult(result);
    setCurrentOperand(formattedResult.toString());
  };

  // Memory functions
  const handleMemoryAdd = () => {
    const value = parseFloat(currentOperand);
    if (!isNaN(value)) {
      setMemory(memory + value);
    }
  };

  const handleMemorySubtract = () => {
    const value = parseFloat(currentOperand);
    if (!isNaN(value)) {
      setMemory(memory - value);
    }
  };

  const handleMemoryRecall = () => {
    setCurrentOperand(memory.toString());
  };

  const handleMemoryClear = () => {
    setMemory(0);
  };

  // Format large numbers
  const formatResult = (num) => {
    // If number is too large or too small, use scientific notation
    if (Math.abs(num) >= 1e15 || (Math.abs(num) < 1e-6 && num !== 0)) {
      return num.toExponential(10);
    }
    // Round to avoid floating point precision issues
    return Math.round(num * 100000000) / 100000000;
  };

  // Perform calculation
  const calculate = () => {
    let result;
    const prev = parseFloat(previousOperand);
    const current = parseFloat(currentOperand);

    if (isNaN(prev) || isNaN(current)) return;

    switch (operation) {
      case '+':
        result = prev + current;
        break;
      case '-':
        result = prev - current;
        break;
      case '*':
        result = prev * current;
        break;
      case '/':
        if (current === 0) {
          alert('Cannot divide by zero!');
          clear();
          return;
        }
        result = prev / current;
        break;
      default:
        return;
    }

    // Format the result
    const formattedResult = formatResult(result);
    
    // Add to history
    const calculation = `${prev} ${operation} ${current} = ${formattedResult}`;
    setHistory([calculation, ...history.slice(0, 9)]);
    
    setCurrentOperand(formattedResult.toString());
    setOperation('');
    setPreviousOperand('');
    setShouldResetDisplay(true);
  };

  // Handle equals button
  const handleEqualsClick = () => {
    if (operation === '' || currentOperand === '' || previousOperand === '') return;
    calculate();
  };

  // Clear all
  const clear = () => {
    setCurrentOperand('0');
    setPreviousOperand('');
    setOperation('');
  };

  // Clear history
  const clearHistory = () => {
    setHistory([]);
  };

  // Format display for previous operand
  const getDisplayValue = () => {
    if (operation && previousOperand) {
      return `${previousOperand} ${operation}`;
    }
    return '';
  };

  return (
    <div className={`App ${darkMode ? 'dark-mode' : 'light-mode'}`}>
      <div className="calculator">
        <div className="calculator-header">
          <h1>Professional Calculator</h1>
          <div className="controls">
            <button 
              className="control-btn" 
              onClick={() => setDarkMode(!darkMode)}
              title="Toggle Theme"
            >
              {darkMode ? '☀️' : '🌙'}
            </button>
            <button 
              className="control-btn" 
              onClick={() => setScientificMode(!scientificMode)}
              title="Toggle Scientific Mode"
            >
              {scientificMode ? '123' : 'f(x)'}
            </button>
            <button 
              className="control-btn" 
              onClick={() => setShowHistory(!showHistory)}
              title="Toggle History"
            >
              📜
            </button>
          </div>
        </div>

        {showHistory && (
          <div className="history-panel">
            <div className="history-header">
              <h3>History</h3>
              <button onClick={clearHistory} className="clear-history">Clear</button>
            </div>
            <div className="history-list">
              {history.length === 0 ? (
                <p className="no-history">No calculations yet</p>
              ) : (
                history.map((item, index) => (
                  <div key={index} className="history-item">{item}</div>
                ))
              )}
            </div>
          </div>
        )}
        
        <div className="display">
          <div className="memory-indicator">
            {memory !== 0 && <span className="memory-badge">M: {memory}</span>}
          </div>
          <div className="previous-operand">{getDisplayValue()}</div>
          <div className="current-operand">{currentOperand}</div>
        </div>

        {scientificMode && (
          <div className="scientific-buttons">
            <button className="scientific" onClick={() => handleScientific('sin')}>sin</button>
            <button className="scientific" onClick={() => handleScientific('cos')}>cos</button>
            <button className="scientific" onClick={() => handleScientific('tan')}>tan</button>
            <button className="scientific" onClick={() => handleScientific('sqrt')}>√</button>
            <button className="scientific" onClick={() => handleScientific('square')}>x²</button>
            <button className="scientific" onClick={() => handleScientific('log')}>log</button>
            <button className="scientific" onClick={() => handleScientific('ln')}>ln</button>
            <button className="scientific" onClick={() => handleScientific('exp')}>eˣ</button>
            <button className="scientific" onClick={() => handleScientific('pi')}>π</button>
            <button className="scientific" onClick={() => handleScientific('e')}>e</button>
          </div>
        )}

        <div className="memory-buttons">
          <button className="memory" onClick={handleMemoryClear}>MC</button>
          <button className="memory" onClick={handleMemoryRecall}>MR</button>
          <button className="memory" onClick={handleMemoryAdd}>M+</button>
          <button className="memory" onClick={handleMemorySubtract}>M-</button>
        </div>

        <div className="buttons">
          <button className="clear" onClick={clear}>AC</button>
          <button className="function" onClick={handleDelete}>⌫</button>
          <button className="function" onClick={handlePercentage}>%</button>
          <button className="operator" onClick={() => handleOperatorClick('/')}>/</button>

          <button className="number" onClick={() => handleNumberClick('7')}>7</button>
          <button className="number" onClick={() => handleNumberClick('8')}>8</button>
          <button className="number" onClick={() => handleNumberClick('9')}>9</button>
          <button className="operator" onClick={() => handleOperatorClick('*')}>×</button>

          <button className="number" onClick={() => handleNumberClick('4')}>4</button>
          <button className="number" onClick={() => handleNumberClick('5')}>5</button>
          <button className="number" onClick={() => handleNumberClick('6')}>6</button>
          <button className="operator" onClick={() => handleOperatorClick('-')}>−</button>

          <button className="number" onClick={() => handleNumberClick('1')}>1</button>
          <button className="number" onClick={() => handleNumberClick('2')}>2</button>
          <button className="number" onClick={() => handleNumberClick('3')}>3</button>
          <button className="operator" onClick={() => handleOperatorClick('+')}>+</button>

          <button className="function" onClick={handleSignChange}>+/-</button>
          <button className="number" onClick={() => handleNumberClick('0')}>0</button>
          <button className="decimal" onClick={handleDecimalClick}>.</button>
          <button className="equals" onClick={handleEqualsClick}>=</button>
        </div>

        <div className="keyboard-hint">
          💡 Keyboard shortcuts: Numbers, +, -, *, /, Enter, Esc, Backspace, %
        </div>
      </div>
    </div>
  );
}

export default App;

\# 🧪 Frontend-Backend Integration Manual Testing Checklist



\## Prerequisites

\- \[ ] Backend server running on http://localhost:5000

\- \[ ] Frontend server running on http://localhost:3000

\- \[ ] Both servers respond to health checks



\## Core Functionality Tests



\### Basic Operations

\- \[ ] Empty string input → Result: 0

\- \[ ] Single number "42" → Result: 42

\- \[ ] Comma separated "1,2,3" → Result: 6

\- \[ ] Large numbers "100,200,300" → Result: 600



\### Delimiter Variations

\- \[ ] Newline separated "1\\n2\\n3" → Result: 6

\- \[ ] Mixed delimiters "1\\n2,3" → Result: 6

\- \[ ] Custom delimiter "//;\\n1;2;3" → Result: 6

\- \[ ] Multi-char delimiter "//\[\*\*\*]\\n1\*\*\*2\*\*\*3" → Result: 6

\- \[ ] Multiple delimiters "//\[\*]\[%]\\n1\*2%3" → Result: 6



\### Edge Cases

\- \[ ] Double commas "1,,2" → Result: 3

\- \[ ] Double newlines "1\\n\\n2" → Result: 3

\- \[ ] Leading/trailing delimiters ",1,2," → Result: 3

\- \[ ] Whitespace " 1 , 2 " → Result: 3



\### UI Behavior

\- \[ ] Loading state appears during calculation

\- \[ ] Buttons disabled during loading

\- \[ ] Success result displays properly

\- \[ ] Error messages show for failures

\- \[ ] Clear button resets form

\- \[ ] Example buttons load correct values



\### History Functionality

\- \[ ] History appears after successful calculation

\- \[ ] History shows correct input and result

\- \[ ] History shows timestamp

\- \[ ] Clear history button works

\- \[ ] History limited to 10 entries



\### Error Handling

\- \[ ] Network error shows user-friendly message

\- \[ ] Backend offline shows connection error

\- \[ ] Timeout shows appropriate message

\- \[ ] Invalid input shows validation error



\### Performance

\- \[ ] Calculations complete within 1 second

\- \[ ] Large inputs (100+ numbers) handle gracefully

\- \[ ] No memory leaks during repeated calculations

\- \[ ] Responsive design works on mobile



\## API Validation

\- \[ ] All requests use correct Content-Type

\- \[ ] All responses have proper JSON structure

\- \[ ] Error responses include success: false

\- \[ ] Success responses include success: true




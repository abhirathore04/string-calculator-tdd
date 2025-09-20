@echo off
echo 🧪 Running Complete Test Suite for String Calculator
echo.

echo ===== Backend Unit Tests =====
cd backend
call venv\Scripts\activate.bat
pytest tests\test_string_calculator.py -v --tb=short
if %ERRORLEVEL% neq 0 goto :error

echo.
echo ===== Backend API Tests =====
pytest tests\test_api.py -v --tb=short
if %ERRORLEVEL% neq 0 goto :error

echo.
echo ===== Integration Tests =====
pytest tests\test_integration.py -v --tb=short
if %ERRORLEVEL% neq 0 goto :error

echo.
echo ===== Frontend Tests =====
cd ..\frontend
npm test -- --coverage --watchAll=false
if %ERRORLEVEL% neq 0 goto :error

echo.
echo ✅ ALL TESTS PASSED! Frontend-Backend Integration Verified!
echo.
echo 📊 Test Coverage:
echo - Backend: 9 test methods, 40+ individual test cases
echo - API: 4 test methods, comprehensive error handling
echo - Integration: 15+ test methods, live server tests
echo - Frontend: 10+ test methods, UI and API interaction
echo.
goto :end

:error
echo.
echo ❌ TESTS FAILED! Check output above for details.
echo.

:end
pause

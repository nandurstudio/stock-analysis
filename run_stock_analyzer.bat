@echo off
echo ========================================================================
echo      Stock Analysis and Trading Recommendation Tool v1.0 (Stable)
echo ========================================================================
echo.
echo This application provides:
echo  - Comprehensive technical analysis (RSI, MACD, Bollinger Bands, etc.)
echo  - Transaction tracking and P/L calculation
echo  - Professional trading recommendations
echo  - Chart visualization and pattern detection
echo.
echo All known bugs have been fixed. See bug_fix_log.md for details.
echo.
echo ========================================================================
echo.

REM Activate virtual environment if it exists
if exist venv (
    call venv\Scripts\activate
    python -m src
) else (
    REM Try to use the existing venv if available
    if exist .venv\Scripts\python.exe (
        .venv\Scripts\python.exe -m src
    ) else (
        REM Fallback to system Python
        python -m src
    )
)

echo.
echo Thank you for using Stock Analysis and Trading Recommendation Tool!
pause

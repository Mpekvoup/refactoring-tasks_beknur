import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Тесты для класса SalaryCalculator.
 */
public class SalaryCalculatorTest {

    private static final double DELTA = 0.001;

    @Test
    public void testCalculateNetSalary() {
        SalaryCalculator calc = new SalaryCalculator(16000, 20, 0.2, 0.05, 0.03);
        // gross = 16000 + (20 * 16000 / 160 * 1.5) = 16000 + 3000 = 19000
        // tax = 19000 * 0.2 = 3800
        // pension = 19000 * 0.05 = 950
        // health = 19000 * 0.03 = 570
        // net = 19000 - 3800 - 950 - 570 = 13680
        assertEquals(13680.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testCalculateGrossSalary() {
        SalaryCalculator calc = new SalaryCalculator(16000, 20, 0.2, 0.05, 0.03);
        // gross = 16000 + (20 * 16000 / 160 * 1.5) = 19000
        assertEquals(19000.0, calc.calculateGrossSalary(), DELTA);
    }

    @Test
    public void testZeroOvertime() {
        SalaryCalculator calc = new SalaryCalculator(16000, 0, 0.2, 0.05, 0.03);
        // gross = 16000, deductions = 16000 * 0.28 = 4480, net = 11520
        assertEquals(11520.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testZeroTax() {
        SalaryCalculator calc = new SalaryCalculator(16000, 20, 0, 0.05, 0.03);
        // gross = 19000, deductions (pension+health) = 19000 * 0.08 = 1520, net = 17480
        assertEquals(17480.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testUpdateSalary() {
        SalaryCalculator calc = new SalaryCalculator(16000, 20, 0.2, 0.05, 0.03);
        calc.updateSalary(18000, 10, 0.25, 0.06, 0.04);

        assertEquals(18000.0, calc.getBaseSalary(), DELTA);
        assertEquals(10, calc.getOvertimeHours());
        assertEquals(0.25, calc.getTaxRate(), DELTA);
        assertEquals(0.06, calc.getPensionRate(), DELTA);
        assertEquals(0.04, calc.getHealthInsuranceRate(), DELTA);

        // gross = 18000 + (10 * 18000 / 160 * 1.5) = 18000 + 1687.5 = 19687.5
        // deductions = 19687.5 * 0.35 = 6890.625
        // net = 12796.875
        assertEquals(12796.875, calc.calculateNetSalary(), DELTA);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeBaseSalaryThrowsException() {
        new SalaryCalculator(-1000, 0, 0.2, 0.05, 0.03);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeOvertimeHoursThrowsException() {
        new SalaryCalculator(16000, -10, 0.2, 0.05, 0.03);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeTaxRateThrowsException() {
        new SalaryCalculator(16000, 0, -0.1, 0.05, 0.03);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testTaxRateAboveOneThrowsException() {
        new SalaryCalculator(16000, 0, 1.5, 0.05, 0.03);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateWithInvalidParametersThrowsException() {
        SalaryCalculator calc = new SalaryCalculator(16000, 0, 0.2, 0.05, 0.03);
        calc.updateSalary(-1000, 0, 0.2, 0.05, 0.03);
    }

    @Test
    public void testGetters() {
        SalaryCalculator calc = new SalaryCalculator(16000, 20, 0.2, 0.05, 0.03);
        assertEquals(16000.0, calc.getBaseSalary(), DELTA);
        assertEquals(20, calc.getOvertimeHours());
        assertEquals(0.2, calc.getTaxRate(), DELTA);
        assertEquals(0.05, calc.getPensionRate(), DELTA);
        assertEquals(0.03, calc.getHealthInsuranceRate(), DELTA);
    }
}

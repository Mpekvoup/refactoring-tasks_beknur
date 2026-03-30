import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Тесты для класса SalaryCalculator.
 */
public class SalaryCalculatorTest {

    private static final double DELTA = 0.001;

    @Test
    public void testCalculateNetSalary() {
        SalaryCalculator calc = new SalaryCalculator(50000, 10000, 0.2);
        // gross = 50000 + 10000 = 60000
        // tax = 60000 * 0.2 = 12000
        // net = 60000 - 12000 = 48000
        assertEquals(48000.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testCalculateGrossSalary() {
        SalaryCalculator calc = new SalaryCalculator(50000, 10000, 0.2);
        assertEquals(60000.0, calc.calculateGrossSalary(), DELTA);
    }

    @Test
    public void testZeroBonus() {
        SalaryCalculator calc = new SalaryCalculator(50000, 0, 0.2);
        assertEquals(40000.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testZeroTax() {
        SalaryCalculator calc = new SalaryCalculator(50000, 10000, 0);
        assertEquals(60000.0, calc.calculateNetSalary(), DELTA);
    }

    @Test
    public void testUpdateSalary() {
        SalaryCalculator calc = new SalaryCalculator(50000, 10000, 0.2);
        calc.updateSalary(60000, 15000, 0.25);

        assertEquals(60000.0, calc.getBaseSalary(), DELTA);
        assertEquals(15000.0, calc.getBonus(), DELTA);
        assertEquals(0.25, calc.getTaxRate(), DELTA);

        // gross = 75000, tax = 18750, net = 56250
        assertEquals(56250.0, calc.calculateNetSalary(), DELTA);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeBaseSalaryThrowsException() {
        new SalaryCalculator(-1000, 5000, 0.2);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeBonusThrowsException() {
        new SalaryCalculator(50000, -5000, 0.2);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeTaxRateThrowsException() {
        new SalaryCalculator(50000, 5000, -0.1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testTaxRateAboveOneThrowsException() {
        new SalaryCalculator(50000, 5000, 1.5);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateWithInvalidParametersThrowsException() {
        SalaryCalculator calc = new SalaryCalculator(50000, 5000, 0.2);
        calc.updateSalary(-1000, 5000, 0.2);
    }

    @Test
    public void testGetters() {
        SalaryCalculator calc = new SalaryCalculator(50000, 10000, 0.2);
        assertEquals(50000.0, calc.getBaseSalary(), DELTA);
        assertEquals(10000.0, calc.getBonus(), DELTA);
        assertEquals(0.2, calc.getTaxRate(), DELTA);
    }
}

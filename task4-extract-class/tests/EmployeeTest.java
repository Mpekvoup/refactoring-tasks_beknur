import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;
import java.util.Date;

/**
 * Интеграционные тесты для рефакторированного класса Employee.
 */
public class EmployeeTest {

    private static final double DELTA = 0.001;
    private Employee employee;
    private Address address;
    private BankDetails bankDetails;
    private SalaryCalculator salaryCalculator;

    @Before
    public void setUp() {
        address = new Address("123 Main St", "New York", "10001", "USA");
        bankDetails = new BankDetails("Chase Bank", "12345678", "123456789");
        salaryCalculator = new SalaryCalculator(50000, 10000, 0.2);

        employee = new Employee(
            "E001",
            "John",
            "Doe",
            new Date(),
            "john.doe@company.com",
            "+1234567890",
            address,
            bankDetails,
            salaryCalculator
        );
    }

    @Test
    public void testEmployeeCreation() {
        assertEquals("E001", employee.getId());
        assertEquals("John", employee.getFirstName());
        assertEquals("Doe", employee.getLastName());
        assertEquals("john.doe@company.com", employee.getEmail());
        assertEquals("+1234567890", employee.getPhone());
    }

    @Test
    public void testGetFullName() {
        assertEquals("John Doe", employee.getFullName());
    }

    @Test
    public void testGetFullAddress() {
        assertEquals("123 Main St, New York, 10001, USA", employee.getFullAddress());
    }

    @Test
    public void testCalculateNetSalary() {
        assertEquals(48000.0, employee.calculateNetSalary(), DELTA);
    }

    @Test
    public void testFormatForPayroll() {
        String payroll = employee.formatForPayroll();
        assertTrue(payroll.contains("E001"));
        assertTrue(payroll.contains("John Doe"));
        assertTrue(payroll.contains("48000.0"));
        assertTrue(payroll.contains("Chase Bank"));
        assertTrue(payroll.contains("12345678"));
    }

    @Test
    public void testUpdateAddress() {
        Address newAddress = new Address("456 Oak Ave", "Boston", "02101", "USA");
        employee.updateAddress(newAddress);

        assertEquals("456 Oak Ave, Boston, 02101, USA", employee.getFullAddress());
    }

    @Test
    public void testUpdateBankDetails() {
        BankDetails newBank = new BankDetails("Wells Fargo", "87654321", "987654321");
        employee.updateBankDetails(newBank);

        assertEquals(newBank, employee.getBankDetails());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateBankDetailsWithInvalid() {
        BankDetails invalidBank = new BankDetails("Wells Fargo", "123", "12345");
        employee.updateBankDetails(invalidBank);
    }

    @Test
    public void testUpdateSalary() {
        employee.updateSalary(60000, 15000, 0.25);
        // gross = 75000, tax = 18750, net = 56250
        assertEquals(56250.0, employee.calculateNetSalary(), DELTA);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullAddressThrowsException() {
        new Employee(
            "E001", "John", "Doe", new Date(),
            "john.doe@company.com", "+1234567890",
            null, bankDetails, salaryCalculator
        );
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullBankDetailsThrowsException() {
        new Employee(
            "E001", "John", "Doe", new Date(),
            "john.doe@company.com", "+1234567890",
            address, null, salaryCalculator
        );
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullSalaryCalculatorThrowsException() {
        new Employee(
            "E001", "John", "Doe", new Date(),
            "john.doe@company.com", "+1234567890",
            address, bankDetails, null
        );
    }

    @Test
    public void testGetAggregatedObjects() {
        assertEquals(address, employee.getAddress());
        assertEquals(bankDetails, employee.getBankDetails());
        assertEquals(salaryCalculator, employee.getSalaryCalculator());
    }

    @Test
    public void testLawOfDemeter() {
        // Правильно: Employee предоставляет делегирующий метод
        String fullAddress = employee.getFullAddress();
        assertEquals("123 Main St, New York, 10001, USA", fullAddress);

        // Правильно: Можем получить объект целиком для передачи дальше
        Address addr = employee.getAddress();
        assertNotNull(addr);

        // Не нарушаем Law of Demeter - не делаем длинные цепочки
    }
}

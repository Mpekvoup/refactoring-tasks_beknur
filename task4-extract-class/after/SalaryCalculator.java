/**
 * Класс для расчета зарплаты сотрудника.
 * Отвечает за всю логику, связанную с зарплатой.
 */
public class SalaryCalculator {
    private double baseSalary;
    private double bonus;
    private double taxRate;

    /**
     * Конструктор калькулятора зарплаты.
     * @param baseSalary базовая зарплата
     * @param bonus бонус
     * @param taxRate налоговая ставка (0.0 - 1.0)
     */
    public SalaryCalculator(double baseSalary, double bonus, double taxRate) {
        if (baseSalary < 0 || bonus < 0 || taxRate < 0 || taxRate > 1) {
            throw new IllegalArgumentException("Invalid salary parameters");
        }
        this.baseSalary = baseSalary;
        this.bonus = bonus;
        this.taxRate = taxRate;
    }

    /**
     * Расчет чистой зарплаты (gross - налоги).
     * @return чистая зарплата после вычета налогов
     */
    public double calculateNetSalary() {
        double gross = baseSalary + bonus;
        double tax = gross * taxRate;
        return gross - tax;
    }

    /**
     * Расчет валовой зарплаты (gross).
     * @return валовая зарплата до вычета налогов
     */
    public double calculateGrossSalary() {
        return baseSalary + bonus;
    }

    /**
     * Обновление параметров зарплаты.
     * @param baseSalary новая базовая зарплата
     * @param bonus новый бонус
     * @param taxRate новая налоговая ставка
     */
    public void updateSalary(double baseSalary, double bonus, double taxRate) {
        if (baseSalary < 0 || bonus < 0 || taxRate < 0 || taxRate > 1) {
            throw new IllegalArgumentException("Invalid salary parameters");
        }
        this.baseSalary = baseSalary;
        this.bonus = bonus;
        this.taxRate = taxRate;
    }

    public double getBaseSalary() { return baseSalary; }
    public double getBonus() { return bonus; }
    public double getTaxRate() { return taxRate; }
}

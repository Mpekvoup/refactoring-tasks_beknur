/**
 * Класс для расчета зарплаты сотрудника.
 * Отвечает за всю логику, связанную с зарплатой.
 */
public class SalaryCalculator {
    private double baseSalary;
    private int overtimeHours;
    private double taxRate;
    private double pensionRate;
    private double healthInsuranceRate;

    /**
     * Конструктор калькулятора зарплаты.
     * @param baseSalary базовая зарплата
     * @param overtimeHours часы сверхурочной работы
     * @param taxRate налоговая ставка (0.0 - 1.0)
     * @param pensionRate ставка пенсионных отчислений (0.0 - 1.0)
     * @param healthInsuranceRate ставка медицинского страхования (0.0 - 1.0)
     */
    public SalaryCalculator(double baseSalary, int overtimeHours, double taxRate,
                           double pensionRate, double healthInsuranceRate) {
        if (baseSalary < 0 || overtimeHours < 0 || taxRate < 0 || taxRate > 1 ||
            pensionRate < 0 || pensionRate > 1 || healthInsuranceRate < 0 || healthInsuranceRate > 1) {
            throw new IllegalArgumentException("Invalid salary parameters");
        }
        this.baseSalary = baseSalary;
        this.overtimeHours = overtimeHours;
        this.taxRate = taxRate;
        this.pensionRate = pensionRate;
        this.healthInsuranceRate = healthInsuranceRate;
    }

    /**
     * Расчет чистой зарплаты (gross - налоги - пенсия - медстраховка).
     * Формула из исходного задания.
     * @return чистая зарплата после вычета налогов и отчислений
     */
    public double calculateNetSalary() {
        double gross = baseSalary + (overtimeHours * baseSalary / 160 * 1.5);
        double tax = gross * taxRate;
        double pension = gross * pensionRate;
        double health = gross * healthInsuranceRate;
        return gross - tax - pension - health;
    }

    /**
     * Расчет валовой зарплаты (gross).
     * @return валовая зарплата до вычета налогов
     */
    public double calculateGrossSalary() {
        return baseSalary + (overtimeHours * baseSalary / 160 * 1.5);
    }

    /**
     * Обновление параметров зарплаты.
     * @param baseSalary новая базовая зарплата
     * @param overtimeHours новые часы сверхурочной работы
     * @param taxRate новая налоговая ставка
     * @param pensionRate новая ставка пенсионных отчислений
     * @param healthInsuranceRate новая ставка медицинского страхования
     */
    public void updateSalary(double baseSalary, int overtimeHours, double taxRate,
                            double pensionRate, double healthInsuranceRate) {
        if (baseSalary < 0 || overtimeHours < 0 || taxRate < 0 || taxRate > 1 ||
            pensionRate < 0 || pensionRate > 1 || healthInsuranceRate < 0 || healthInsuranceRate > 1) {
            throw new IllegalArgumentException("Invalid salary parameters");
        }
        this.baseSalary = baseSalary;
        this.overtimeHours = overtimeHours;
        this.taxRate = taxRate;
        this.pensionRate = pensionRate;
        this.healthInsuranceRate = healthInsuranceRate;
    }

    public double getBaseSalary() { return baseSalary; }
    public int getOvertimeHours() { return overtimeHours; }
    public double getTaxRate() { return taxRate; }
    public double getPensionRate() { return pensionRate; }
    public double getHealthInsuranceRate() { return healthInsuranceRate; }
}

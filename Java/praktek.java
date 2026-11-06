import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class Praktek {
    public static void main(string[] args) {
        LocalDate hari = LocalDate.now();
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern(
            "EEEE, dd MMMM YYYY",
            Locale.forLanguageTag("id-ID"));
        System.out.println("Hari ini " + hari.format(fmt)
            + ", saya belajar library di java");
    }
}
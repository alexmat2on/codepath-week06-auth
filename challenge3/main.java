import java.*;
import java.time.LocalDateTime;
import java.time.*;
import java.time.format.DateTimeFormatter;

public class main {
    public static void main(String[] args) {
        System.out.println(LocalDateTime.now());

        System.out.println(ZonedDateTime.now().format(DateTimeFormatter.RFC_1123_DATE_TIME));
    }
}

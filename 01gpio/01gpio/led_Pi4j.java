import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class GPIO_Pi4j {

    public static void main(String[] args) throws InterruptedException {

        final GpioController gpio = GpioFactory.getInstance();
        final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "MyLED", PinState.HIGH);

        pin.setShutdownOptions(true, PinState.LOW);
        for(int i=0; i<5; i++){
        	pin.high();
	        System.out.println("--> GPIO state should be: ON");
	        Thread.sleep(1000);
	        pin.low();
	        System.out.println("--> GPIO state should be: OFF");
	        Thread.sleep(1000);
        }
        System.out.println("Exiting ControlGpioExample");
    }
}
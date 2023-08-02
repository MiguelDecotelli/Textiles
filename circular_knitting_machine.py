import time

class CircularKnittingMachine:
    def __init__(self, num_needles):
        self.needles = [True] * num_needles
        self.is_running = False

    def check_needles(self):
        if self.is_running:
            for idx, needle_status in enumerate(self.needles):
                if not needle_status:
                    print(f"Needle detected error {idx + 1}. Interrupting production.")
                    self.stop_production()
                    break
            else:
                print("Knitting...")

    def start_production(self):
        self.is_running = True
        print("Starting production.")

    def stop_production(self):
        self.is_running = False
        print("Production stopped.")

class DefectDetector:
    def __init__(self):
        self.defects = set()

    def detect_defects(self, fabric_type, yarn_type, defects_found):
        key = (fabric_type, yarn_type)
        self.defects.add((key, defects_found))

    def check_for_defects(self, knitting_machine):
        for defects_found in self.defects:
            if any(defect in ["Thick Yarn", "Hole"] for defect in defects_found):
                print("Defect detected on production. Stopping machinery.")
                knitting_machine.stop_production()
                break

def main():
    knitting_machine = CircularKnittingMachine(num_needles=600)
    defect_detector = DefectDetector()

    knitting_machine.start_production()

    defect_detector.detect_defects("Single Jersey", "Conventional Cotton", ["Thick Yarn", "Hole"])
    defect_detector.detect_defects("Interlock", "Polyester", ["Broken Elastane", "Oil"])
    defect_detector.detect_defects("Pique", "Organic Cotton", ["Sinker", "Thin Yarn"])
    defect_detector.detect_defects("French Terry", "Lyocell", ["Elastane Dashes"])
    defect_detector.detect_defects("Jersey", "Viscose", ["Hole"])  # Simulação de defeito detectado

    for _ in range(20):
        time.sleep(1)
        knitting_machine.check_needles()
        defect_detector.check_for_defects(knitting_machine)

if __name__ == "__main__":
    main()

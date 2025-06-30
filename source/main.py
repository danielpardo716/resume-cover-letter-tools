from resume_parser import ResumeParser

def main():
    parser = ResumeParser("examples/example-resume.yaml")
    print(parser.get_contact())

if __name__ == "__main__":
    main()

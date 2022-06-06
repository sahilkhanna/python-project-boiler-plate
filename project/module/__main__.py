from project import Project

def main():
    print("Called from main()")
    p = Project()
    p.main()

if __name__ == "__main__":
    print("Called from __main__.py")
    main()
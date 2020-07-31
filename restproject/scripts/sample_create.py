from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet1 = Snippet(title='1st Code', code='a = int(input())\n', linenos=True)
snippet1.save()

snippet2 = Snippet(title='2nd Code', code='public class Main{\n\tpublic static void main(String[] args){\n\t\tint a=2;\n\t\tSystem.out.println(a);\n\t}\n}', linenos=False, language='java')
snippet2.save()

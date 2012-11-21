import sublime_plugin
import webbrowser

# -------------------------------------------
# { "keys": ["super+shift+a"], "command": "open_drupalapi" }
# -------------------------------------------


# Open the URL in the current selection
class GotoDrupalapiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                word = self.view.word(region)
                keyword = self.view.substr(word)
                webbrowser.open_new_tab("http://api.drupal.org/api/search/7/%s" % keyword)

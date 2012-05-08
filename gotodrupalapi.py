import sublime
import sublime_plugin


# -------------------------------------------
# { "keys": ["super+shift+a"], "command": "open_drupalapi" }
# -------------------------------------------

def open_url(url):
    sublime.active_window().run_command('open_url', {"url": url})


# Open the URL in the current selection
class GotoDrupalapiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                word = self.view.word(region)
                keyword = self.view.substr(word)
                open_url("http://api.drupal.org/api/search/7/%s" % keyword)

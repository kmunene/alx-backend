<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">Pagination</h1>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Learning Objectives</h2>
<p style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/zQ78qQVUjaPExupXQpAaHw" title="explain to anyone" target="_blank" style="color: transparent;">explain to anyone</a>, <strong><strong>without the help of Google</strong></strong>:</p>
<ul style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <li>How to paginate a dataset with simple page and page_size parameters</li>
    <li>How to paginate a dataset with hypermedia metadata</li>
    <li>How to paginate in a deletion-resilient manner</li>
</ul>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Simple helper function</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Write a function named <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index_range</code> that takes two integer arguments <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code>.</p>
            <p>The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.</p>
            <p>Page numbers are 1-indexed, i.e. the first page is page 1.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

index_range = __import__(&apos;0-simple_helper_function&apos;).index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
&lt;class &apos;tuple&apos;&gt;
(0, 7)
&lt;class &apos;tuple&apos;&gt;
(30, 45)
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x00-pagination</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0-simple_helper_function.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">1. Simple pagination</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Copy <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index_range</code> from the previous task and the following class into your code</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">import csv
import math
from typing import List


class Server:
    &quot;&quot;&quot;Server class to paginate a database of popular baby names.
    &quot;&quot;&quot;
    DATA_FILE = &quot;Popular_Baby_Names.csv&quot;

    def __init__(self):
        self.__dataset = None

    def dataset(self) -&gt; List[List]:
        &quot;&quot;&quot;Cached dataset
        &quot;&quot;&quot;
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -&gt; List[List]:
            pass
</code></pre>
            <p>Implement a method named <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">get_page</code> that takes two integer arguments <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page</code> with default value 1 and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code> with default value 10.</p>
            <ul>
                <li>You have to use this <a href="https://intranet.alxswe.com/rltoken/NBLY6mdKDBR9zWvNADwjjg" title="CSV file" target="_blank" style="color: transparent;">CSV file</a> (same as the one presented at the top of the project)</li>
                <li>Use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">assert</code> to verify that both arguments are integers greater than 0.</li>
                <li>Use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index_range</code> to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).</li>
                <li>If the input arguments are out of range for the dataset, an empty list should be returned.</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$  wc -l Popular_Baby_Names.csv 
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child&apos;s First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$  
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&apos;1-simple_pagination&apos;).Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print(&quot;AssertionError raised with negative values&quot;)

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print(&quot;AssertionError raised with 0&quot;)

try:
    should_err = server.get_page(2, &apos;Bob&apos;)
except AssertionError:
    print(&quot;AssertionError raised when page and/or page_size are not ints&quot;)


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Olivia&apos;, &apos;172&apos;, &apos;1&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Chloe&apos;, &apos;112&apos;, &apos;2&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Sophia&apos;, &apos;104&apos;, &apos;3&apos;]]
[[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Emily&apos;, &apos;99&apos;, &apos;4&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Mia&apos;, &apos;79&apos;, &apos;5&apos;]]
[]
bob@dylan:~$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x00-pagination</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">1-simple_pagination.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">2. Hypermedia pagination</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Replicate code from the previous task.</p>
            <p>Implement a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">get_hyper</code> method that takes the same arguments (and defaults) as <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">get_page</code> and returns a dictionary containing the following key-value pairs:</p>
            <ul>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code>: the length of the returned dataset page</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page</code>: the current page number</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">data</code>: the dataset page (equivalent to return from previous task)</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">next_page</code>: number of the next page, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if no next page</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">prev_page</code>: number of the previous page, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if no previous page</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">total_pages</code>: the total number of pages in the dataset as an integer</li>
            </ul>
            <p>Make sure to reuse <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">get_page</code> in your implementation.</p>
            <p>You can use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">math</code> module if necessary.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&apos;2-hypermedia_pagination&apos;).Server

server = Server()

print(server.get_hyper(1, 2))
print(&quot;---&quot;)
print(server.get_hyper(2, 2))
print(&quot;---&quot;)
print(server.get_hyper(100, 3))
print(&quot;---&quot;)
print(server.get_hyper(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./2-main.py
{&apos;page_size&apos;: 2, &apos;page&apos;: 1, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Olivia&apos;, &apos;172&apos;, &apos;1&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Chloe&apos;, &apos;112&apos;, &apos;2&apos;]], &apos;next_page&apos;: 2, &apos;prev_page&apos;: None, &apos;total_pages&apos;: 9709}
---
{&apos;page_size&apos;: 2, &apos;page&apos;: 2, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Sophia&apos;, &apos;104&apos;, &apos;3&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Emma&apos;, &apos;99&apos;, &apos;4&apos;]], &apos;next_page&apos;: 3, &apos;prev_page&apos;: 1, &apos;total_pages&apos;: 9709}
---
{&apos;page_size&apos;: 3, &apos;page&apos;: 100, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;BLACK NON HISPANIC&apos;, &apos;Londyn&apos;, &apos;14&apos;, &apos;39&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;BLACK NON HISPANIC&apos;, &apos;Amirah&apos;, &apos;14&apos;, &apos;39&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;BLACK NON HISPANIC&apos;, &apos;McKenzie&apos;, &apos;14&apos;, &apos;39&apos;]], &apos;next_page&apos;: 101, &apos;prev_page&apos;: 99, &apos;total_pages&apos;: 6473}
---
{&apos;page_size&apos;: 0, &apos;page&apos;: 3000, &apos;data&apos;: [], &apos;next_page&apos;: None, &apos;prev_page&apos;: 2999, &apos;total_pages&apos;: 195}
bob@dylan:~$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x00-pagination</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">2-hypermedia_pagination.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">3. Deletion-resilient hypermedia pagination</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.</p>
            <p>Start <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">3-hypermedia_del_pagination.py</code> with this code:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">#!/usr/bin/env python3
&quot;&quot;&quot;
Deletion-resilient hypermedia pagination
&quot;&quot;&quot;

import csv
import math
from typing import List


class Server:
    &quot;&quot;&quot;Server class to paginate a database of popular baby names.
    &quot;&quot;&quot;
    DATA_FILE = &quot;Popular_Baby_Names.csv&quot;

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -&gt; List[List]:
        &quot;&quot;&quot;Cached dataset
        &quot;&quot;&quot;
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -&gt; Dict[int, List]:
        &quot;&quot;&quot;Dataset indexed by sorting position, starting at 0
        &quot;&quot;&quot;
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -&gt; Dict:
            pass
</code></pre>
            <p>Implement a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">get_hyper_index</code> method with two integer arguments: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index</code> with a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> default value and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code> with default value of 10.</p>
            <ul>
                <li>The method should return a dictionary with the following key-value pairs:<ul>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index</code>: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code> 20, and no data was removed from the dataset, the current index should be 60.</li>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">next_index</code>: the next index to query with. That should be the index of the first item after the last item on the current page.</li>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code>: the current page size</li>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">data</code>: the actual page of the dataset</li>
                    </ul>
                </li>
            </ul>
            <p><strong><strong>Requirements/Behavior</strong></strong>:</p>
            <ul>
                <li>Use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">assert</code> to verify that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">index</code> is in a valid range.</li>
                <li>If the user queries index 0, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code> 10, they will get rows indexed 0 to 9 included.</li>
                <li>If they request the next index (10) with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">page_size</code> 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&apos;3-hypermedia_del_pagination&apos;).Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print(&quot;AssertionError raised when out of range&quot;)        


index = 3
page_size = 2

print(&quot;Nb items: {}&quot;.format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get(&apos;next_index&apos;), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get(&apos;index&apos;)]
print(&quot;Nb items: {}&quot;.format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -&gt; the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -&gt; same data page as the request 2-
print(server.get_hyper_index(res.get(&apos;next_index&apos;), page_size))

bob@dylan:~$ 
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{&apos;index&apos;: 3, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Emma&apos;, &apos;99&apos;, &apos;4&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Emily&apos;, &apos;99&apos;, &apos;4&apos;]], &apos;page_size&apos;: 2, &apos;next_index&apos;: 5}
{&apos;index&apos;: 5, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Mia&apos;, &apos;79&apos;, &apos;5&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Charlotte&apos;, &apos;59&apos;, &apos;6&apos;]], &apos;page_size&apos;: 2, &apos;next_index&apos;: 7}
Nb items: 19417
{&apos;index&apos;: 3, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Emily&apos;, &apos;99&apos;, &apos;4&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Mia&apos;, &apos;79&apos;, &apos;5&apos;]], &apos;page_size&apos;: 2, &apos;next_index&apos;: 6}
{&apos;index&apos;: 5, &apos;data&apos;: [[&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Mia&apos;, &apos;79&apos;, &apos;5&apos;], [&apos;2016&apos;, &apos;FEMALE&apos;, &apos;ASIAN AND PACIFIC ISLANDER&apos;, &apos;Charlotte&apos;, &apos;59&apos;, &apos;6&apos;]], &apos;page_size&apos;: 2, &apos;next_index&apos;: 7}
bob@dylan:~$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x00-pagination</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">3-hypermedia_del_pagination.py</code></li>
                </ul>
            </div>
        </div>
    </div>
</div>
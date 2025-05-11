<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Table</title>
    <style>
        table {
            border-spacing: 0;
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
            border: 3px solid #000000;
        }
        td {
            text-align: center;
            vertical-align: middle;
            padding: 10px;
            border: 1px solid #000000;
            height: 50px;
            cursor: pointer;
        }
        .header {
            font-weight: bold;
            background-color: #E8E8E8;
        }
        .first-col {
            background-color: #61cbf3;
        }
        .second-col {
            background-color: #94dcf8;
        }
        .selected {
            background-color: #92D050 !important;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <td class="header" style="width: 160px;">Category</td>
            <td class="header" style="width: 200px;">Dimension</td>
            <td class="header" colspan="6">Attributes</td>
        </tr>
        <tr>
            <td class="first-col" rowspan="4">Impact (What)</td>
            <td class="second-col">Benefits</td>
            <td>Quality/Scope/Knowledge</td>
            <td>Time Efficiency</td>
            <td>Cost</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="second-col">Focus within Business Model Navigator</td>
            <td>Customer Segments</td>
            <td>Value Proposition</td>
            <td>Value Chain</td>
            <td>Revenue Model</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="second-col">Aim</td>
            <td>Product Innovation</td>
            <td>Process Innovation</td>
            <td>Business Model Innovation</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="second-col">Ambidexterity</td>
            <td>Exploration</td>
            <td>Exploitation</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="first-col" rowspan="5">Technology (How)</td>
            <td class="second-col">AI Role</td>
            <td>Automaton</td>
            <td>Helper</td>
            <td>Partner</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="second-col">AI Concepts</td>
            <td>Machine Learning</td>
            <td>Deep Learning</td>
            <td>Artificial Neural Networks</td>
            <td>Natural Language Processing</td>
            <td>Computer Vision</td>
            <td>Robotics</td>
        </tr>
        <!-- Add more rows as needed -->
    </table>

    <script>
        // Function to handle cell click
        function handleCellClick(element) {
            if (element.classList.contains('selected')) {
                element.classList.remove('selected');
            } else {
                element.classList.add('selected');
            }
        }

        // Add event listeners to all table cells
        document.querySelectorAll('td').forEach(cell => {
            cell.addEventListener('click', () => handleCellClick(cell));
        });
    </script>
</body>
</html>

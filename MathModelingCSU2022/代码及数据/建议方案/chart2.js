import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
        }
    },
    legend: {
        data: ['Ǹ����', '������', 'ƽ�����������']
    },
    xAxis: [
        {
            type: 'category',
            data: ['ˮ��', '����', '����', '����', 'С��', '����', '����', '��', '������'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '�������꣩',
            min: 0,
            max: 20,
            interval: 5,
            axisLabel: {
                formatter: '{value}'
            }
        },
        {
            type: 'value',
            name: 'ƽ�����������',
            min: -10,
            max: 0,
            interval: 2,
            axisLabel: {
                formatter: '{value} %'
            }
        }
    ],
    series: [
        {
            name: 'Ǹ����',
            type: 'bar',
            tooltip: {
                valueFormatter: function (value) {
                    return value;
                }
            },
            data: [
                16, 14, 15, 16, 14, 13, 17, 17, 14
            ]
        },
        {
            name: '������',
            type: 'bar',
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' ml';
                }
            },
            data: [
                2, 4, 2, 5, 5, 7, 6, 3, 7
            ]
        },
        {
            name: 'ƽ�����������',
            type: 'line',
            yAxisIndex: 1,
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' ��C';
                }
            },
            data: [-2.48, -3.36, -2.36, -4.49, -5.93, -5.75, -5.95, -3.74, -7.17]
        }
    ]
};

option && myChart.setOption(option);

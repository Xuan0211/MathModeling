import * as echarts from 'echarts';

type EChartsOption = echarts.EChartsOption;

var chartDom = document.getElementById('main')!;
var myChart = echarts.init(chartDom);
var option: EChartsOption;

option = {
    title: {
        text: '2018��������Ҫ������ɫ�����ṹ'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data: ['ԭ��', '��Ȼ��', 'ԭ ú', '����', 'ˮ������', '������Դ', '����']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            boundaryGap: false,
            data: [
                '������',
                '��������',
                'ŷ ��',
                '��  ��',
                '��  ��',
                '��̫����',
                '��  ��'
            ]
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: 'ԭ��',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [0.5, 6.9, 1.4, 25.1, 9.1, 1.5, 3.0]
        },
        {
            name: '��Ȼ��',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [33.7, 17.5, 17.9, 70.8, 39.7, 12.1, 23.2]
        },
        {
            name: 'ԭ ú',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [24.5, 5.9, 21.2, 1.7, 30.0, 59.4, 38.0]
        },
        {
            name: '����',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [17.7, 1.7, 23.0, 0.6, 1.3, 4.5, 10.1]
        },
        {
            name: 'ˮ������',
            type: 'line',
            stack: 'Total',
            label: {
                show: true,
                position: 'top'
            },
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [13.0, 56.0, 15.5, 1.2, 15.6, 14.0, 15.8]
        },
        {
            name: '������Դ',
            type: 'line',
            stack: 'Total',
            label: {
                show: true,
                position: 'top'
            },
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [9.6, 12.0, 18.7, 0.6, 3.7, 8.1, 9.3]
        },
        {
            name: '�� ��',
            type: 'line',
            stack: 'Total',
            label: {
                show: true,
                position: 'top'
            },
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [0.3, 0.04, 2.2, 0, 0.6, 0.3, 0.6]
        }
    ]
};

option && myChart.setOption(option);


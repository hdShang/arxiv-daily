---
layout: default
title: AndesVL Technical Report: An Efficient Mobile-side Multimodal Large Language Model
---

# AndesVL Technical Report: An Efficient Mobile-side Multimodal Large Language Model

**arXiv**: [2510.11496v1](https://arxiv.org/abs/2510.11496) | [PDF](https://arxiv.org/pdf/2510.11496.pdf)

**作者**: Zhiwei Jin, Xiaohui Song, Nan Wang, Yafei Liu, Chao Li, Xin Li, Ruichen Wang, Zhihao Li, Qi Qi, Long Cheng, Dongze Hao, Quanlong Zheng, Yanhao Zhang, Haobo Ji, Jian Ma, Zhitong Zheng, Zhenyi Lin, Haolin Deng, Xin Zou, Xiaojie Yin, Ruilin Wang, Liankai Cai, Haijing Liu, Yuqing Qiu, Ke Chen, Zixian Li, Chi Xie, Huafei Li, Chenxing Li, Chuangchuang Wang, Kai Tang, Zhiguang Zhu, Kai Tang, Wenmei Gao, Rui Wang, Jun Wu, Chao Liu, Qin Xie, Chen Chen, Haonan Lu

---

## 💡 一句话要点

**提出AndesVL移动端多模态大模型，以解决边缘设备资源限制问题**

**关键词**: `移动端多模态模型` `参数高效设计` `视觉语言理解` `边缘计算优化` `多任务基准测试`

## 📋 核心要点

1. 核心问题：云端大模型参数庞大，无法在移动设备上高效运行
2. 方法要点：基于Qwen3 LLM和视觉编码器，构建0.6B至4B参数模型
3. 实验或效果：在多项开源基准测试中达到同类模型领先水平

## 📄 摘要（原文）

> In recent years, while cloud-based MLLMs such as QwenVL, InternVL, GPT-4o,
> Gemini, and Claude Sonnet have demonstrated outstanding performance with
> enormous model sizes reaching hundreds of billions of parameters, they
> significantly surpass the limitations in memory, power consumption, and
> computing capacity of edge devices such as mobile phones. This paper introduces
> AndesVL, a suite of mobile-side MLLMs with 0.6B to 4B parameters based on
> Qwen3's LLM and various visual encoders. We comprehensively outline the model
> architectures, training pipeline, and training data of AndesVL, which achieves
> first-tier performance across a wide range of open-source benchmarks, including
> fields such as text-rich image understanding, reasoning and math, multi-image
> comprehension, general VQA, hallucination mitigation, multilingual
> understanding, and GUI-related tasks when compared with state-of-the-art models
> of a similar scale. Furthermore, we introduce a 1+N LoR


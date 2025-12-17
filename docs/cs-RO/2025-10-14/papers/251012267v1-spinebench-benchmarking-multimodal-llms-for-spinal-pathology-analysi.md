---
layout: default
title: SpineBench: Benchmarking Multimodal LLMs for Spinal Pathology Analysis
---

# SpineBench: Benchmarking Multimodal LLMs for Spinal Pathology Analysis

**arXiv**: [2510.12267v1](https://arxiv.org/abs/2510.12267) | [PDF](https://arxiv.org/pdf/2510.12267.pdf)

**作者**: Chenghanyu Zhang, Zekun Li, Peipei Li, Xing Cui, Shuhan Xia, Weixiang Yan, Yiqiao Zhang, Qianyu Zhuang

---

## 💡 一句话要点

**提出SpineBench基准以评估多模态大语言模型在脊柱病理分析中的性能**

**关键词**: `多模态大语言模型` `脊柱病理分析` `视觉问答基准` `医学图像评估` `疾病诊断` `病灶定位`

## 📋 核心要点

1. 现有基准在脊柱等依赖视觉输入的领域评估不足，无法捕捉细粒度性能。
2. 构建包含64,878个问答对的VQA基准，覆盖11种脊柱疾病，模拟真实挑战场景。
3. 评估12个领先MLLM，结果显示模型在脊柱任务中表现不佳，指导未来改进。

## 📄 摘要（原文）

> With the increasing integration of Multimodal Large Language Models (MLLMs)
> into the medical field, comprehensive evaluation of their performance in
> various medical domains becomes critical. However, existing benchmarks
> primarily assess general medical tasks, inadequately capturing performance in
> nuanced areas like the spine, which relies heavily on visual input. To address
> this, we introduce SpineBench, a comprehensive Visual Question Answering (VQA)
> benchmark designed for fine-grained analysis and evaluation of MLLMs in the
> spinal domain. SpineBench comprises 64,878 QA pairs from 40,263 spine images,
> covering 11 spinal diseases through two critical clinical tasks: spinal disease
> diagnosis and spinal lesion localization, both in multiple-choice format.
> SpineBench is built by integrating and standardizing image-label pairs from
> open-source spinal disease datasets, and samples challenging hard negative
> options for each VQA pair based on visual similarity (similar but not the same
> disease), simulating real-world challenging scenarios. We evaluate 12 leading
> MLLMs on SpineBench. The results reveal that these models exhibit poor
> performance in spinal tasks, highlighting limitations of current MLLM in the
> spine domain and guiding future improvements in spinal medicine applications.
> SpineBench is publicly available at
> https://zhangchenghanyu.github.io/SpineBench.github.io/.


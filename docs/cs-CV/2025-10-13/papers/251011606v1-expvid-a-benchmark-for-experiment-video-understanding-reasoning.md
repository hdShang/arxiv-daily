---
layout: default
title: ExpVid: A Benchmark for Experiment Video Understanding & Reasoning
---

# ExpVid: A Benchmark for Experiment Video Understanding & Reasoning

**arXiv**: [2510.11606v1](https://arxiv.org/abs/2510.11606) | [PDF](https://arxiv.org/pdf/2510.11606.pdf)

**作者**: Yicheng Xu, Yue Wu, Jiashuo Yu, Ziang Yan, Tianxiang Jiang, Yinan He, Qingsong Zhao, Kai Chen, Yu Qiao, Limin Wang, Manabu Okumura, Yi Wang

---

## 💡 一句话要点

**提出ExpVid基准以评估多模态大模型在科学实验视频理解中的能力**

**关键词**: `多模态大模型` `科学实验视频` `基准评估` `细粒度感知` `过程理解` `科学推理`

## 📋 核心要点

1. 现有基准忽略湿实验室工作的细粒度和长程特性，难以评估MLLMs的真实能力
2. 引入三级任务层次：细粒度感知、过程理解和科学推理，确保视觉基础
3. 评估19个MLLMs，发现其在细粒度细节和推理方面表现不佳，开源模型差距显著

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) hold promise for accelerating
> scientific discovery by interpreting complex experimental procedures. However,
> their true capabilities are poorly understood, as existing benchmarks neglect
> the fine-grained and long-horizon nature of authentic laboratory work,
> especially in wet-lab settings. To bridge this gap, we introduce ExpVid, the
> first benchmark designed to systematically evaluate MLLMs on scientific
> experiment videos. Curated from peer-reviewed video publications, ExpVid
> features a new three-level task hierarchy that mirrors the scientific process:
> (1) Fine-grained Perception of tools, materials, and actions; (2) Procedural
> Understanding of step order and completeness; and (3) Scientific Reasoning that
> connects the full experiment to its published conclusions. Our vision-centric
> annotation pipeline, combining automated generation with multi-disciplinary
> expert validation, ensures that tasks require visual grounding. We evaluate 19
> leading MLLMs on ExpVid and find that while they excel at coarse-grained
> recognition, they struggle with disambiguating fine details, tracking state
> changes over time, and linking experimental procedures to scientific outcomes.
> Our results reveal a notable performance gap between proprietary and
> open-source models, particularly in high-order reasoning. ExpVid not only
> provides a diagnostic tool but also charts a roadmap for developing MLLMs
> capable of becoming trustworthy partners in scientific experimentation.


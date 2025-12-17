---
layout: default
title: JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor-Evaluator Optimization
---

# JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor-Evaluator Optimization

**arXiv**: [2511.23002v1](https://arxiv.org/abs/2511.23002) | [PDF](https://arxiv.org/pdf/2511.23002.pdf)

**作者**: Yunlong Lin, Linqing Wang, Kunjie Lin, Zixu Lin, Kaixiong Gong, Wenbo Li, Bin Lin, Zhenxi Li, Shiyi Zhang, Yuyang Peng, Wenxun Dai, Xinghao Ding, Chunyu Wang, Qinglin Lu

---

## 💡 一句话要点

**提出JarvisEvo自进化图像编辑代理，通过协同编辑-评估优化解决指令幻觉和奖励黑客问题。**

**关键词**: `图像编辑代理` `多模态思维链` `协同优化` `自进化学习` `Adobe Lightroom集成`

## 📋 核心要点

1. 核心问题：图像编辑代理存在指令幻觉和奖励黑客，导致事实错误和奖励函数滥用。
2. 方法要点：采用交错多模态思维链推理和协同编辑-评估策略优化框架，实现无外部奖励的自改进。
3. 实验或效果：在ArtEdit-Bench上，JarvisEvo在保护性编辑指标上平均优于Nano-Banana 18.95%。

## 📄 摘要（原文）

> Agent-based editing models have substantially advanced interactive experiences, processing quality, and creative flexibility. However, two critical challenges persist: (1) instruction hallucination, text-only chain-of-thought (CoT) reasoning cannot fully prevent factual errors due to inherent information bottlenecks; (2) reward hacking, dynamic policy optimization against static reward models allows agents to exploit flaws in reward functions. To address these issues, we propose JarvisEvo, a unified image editing agent that emulates an expert human designer by iteratively editing, selecting appropriate tools, evaluating results, and reflecting on its own decisions to refine outcomes. JarvisEvo offers three key advantages: (1) an interleaved multimodal chain-of-thought (iMCoT) reasoning mechanism that enhances instruction following and editing quality; (2) a synergistic editor-evaluator policy optimization (SEPO) framework that enables self-improvement without external rewards, effectively mitigating reward hacking; and (3) support for both global and local fine-grained editing through seamless integration of Adobe Lightroom. On ArtEdit-Bench, JarvisEvo outperforms Nano-Banana by an average of 18.95% on preservative editing metrics, including a substantial 44.96% improvement in pixel-level content fidelity.


---
layout: default
title: OmniGuard: Unified Omni-Modal Guardrails with Deliberate Reasoning
---

# OmniGuard: Unified Omni-Modal Guardrails with Deliberate Reasoning

**arXiv**: [2512.02306v1](https://arxiv.org/abs/2512.02306) | [PDF](https://arxiv.org/pdf/2512.02306.pdf)

**作者**: Boyu Zhu, Xiaofei Wen, Wenjie Jacky Mo, Tinghui Zhu, Yanan Xie, Peng Qi, Muhao Chen

---

## 💡 一句话要点

**提出OmniGuard统一全模态护栏，通过深思推理解决多模态大模型安全挑战。**

**关键词**: `全模态大模型` `安全护栏` `深思推理` `多模态安全数据集` `跨模态泛化` `统一框架`

## 📋 核心要点

1. 全模态大模型处理文本、图像、视频和音频，现有护栏研究多为单模态且依赖二元分类，缺乏跨模态鲁棒性。
2. OmniGuard首次实现全模态护栏，具备深思推理能力，基于超过21万多样本的全模态安全数据集训练，样本覆盖单模态和跨模态输入。
3. 在15个基准测试中，OmniGuard展现出强效性和泛化能力，为构建更稳健的全模态安全系统提供统一框架。

## 📄 摘要（原文）

> Omni-modal Large Language Models (OLLMs) that process text, images, videos, and audio introduce new challenges for safety and value guardrails in human-AI interaction. Prior guardrail research largely targets unimodal settings and typically frames safeguarding as binary classification, which limits robustness across diverse modalities and tasks. To address this gap, we propose OmniGuard, the first family of omni-modal guardrails that performs safeguarding across all modalities with deliberate reasoning ability. To support the training of OMNIGUARD, we curate a large, comprehensive omni-modal safety dataset comprising over 210K diverse samples, with inputs that cover all modalities through both unimodal and cross-modal samples. Each sample is annotated with structured safety labels and carefully curated safety critiques from expert models through targeted distillation. Extensive experiments on 15 benchmarks show that OmniGuard achieves strong effectiveness and generalization across a wide range of multimodal safety scenarios. Importantly, OmniGuard provides a unified framework that enforces policies and mitigates risks in omni-modalities, paving the way toward building more robust and capable omnimodal safeguarding systems.


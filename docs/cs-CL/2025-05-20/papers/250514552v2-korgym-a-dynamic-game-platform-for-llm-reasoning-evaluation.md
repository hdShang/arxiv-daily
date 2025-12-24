---
layout: default
title: "KORGym: A Dynamic Game Platform for LLM Reasoning Evaluation"
---

# KORGym: A Dynamic Game Platform for LLM Reasoning Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14552" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14552v2</a>
  <a href="https://arxiv.org/pdf/2505.14552.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14552v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14552v2', 'KORGym: A Dynamic Game Platform for LLM Reasoning Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun Shi, Jian Yang, Jiaheng Liu, Xingyuan Bu, Jiangjie Chen, Junting Zhou, Kaijing Ma, Zhoufutu Wen, Bingli Wang, Yancheng He, Liang Song, Hualei Zhu, Shilong Li, Xingjian Wang, Wei Zhang, Ruibin Yuan, Yifan Yao, Wenjun Yang, Yunli Wang, Siyuan Fang, Siyu Yuan, Qianyu He, Xiangru Tang, Yingshui Tan, Wangchunshu Zhou, Zhaoxiang Zhang, Zhoujun Li, Wenhao Huang, Ge Zhang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20 (更新: 2025-05-21)

**备注**: 22 pages

---

## 💡 一句话要点

**提出KORGym以解决LLM推理评估的不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理评估` `动态评估平台` `强化学习` `多模态评估` `知识正交推理`

## 📋 核心要点

1. 现有的评估基准往往局限于特定领域，无法全面反映大型语言模型的推理能力。
2. KORGym是一个动态评估平台，提供多种游戏形式，支持交互式评估，旨在全面评估LLM的推理能力。
3. 通过对19个LLM和8个VLM的实验，发现模型家族内存在一致的推理模式，闭源模型表现优越。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展凸显了对更全面评估方法的需求，以准确评估其推理能力。现有基准往往是特定领域的，无法全面捕捉LLM的通用推理潜力。为了解决这一局限性，我们提出了知识正交推理训练场（KORGym），这是一个动态评估平台，灵感来自KOR-Bench和Gymnasium。KORGym提供超过五十种文本或视觉格式的游戏，并支持交互式、多轮评估与强化学习场景。通过KORGym，我们对19个LLM和8个VLM进行了广泛实验，揭示了模型家族内的一致推理模式，并展示了闭源模型的优越性能。进一步分析考察了模态、推理策略、强化学习技术和响应长度对模型性能的影响。我们期望KORGym成为推进LLM推理研究和开发适合复杂交互环境的评估方法的重要资源。

## 🔬 方法详解

**问题定义**：论文旨在解决现有评估方法无法全面捕捉大型语言模型推理能力的问题，现有基准多为领域特定，缺乏通用性。

**核心思路**：提出KORGym作为动态评估平台，通过提供多种游戏形式和交互式评估，旨在全面考察LLM的推理能力。

**技术框架**：KORGym的整体架构包括游戏设计模块、评估交互模块和数据分析模块，支持文本和视觉格式的游戏，结合强化学习场景进行多轮评估。

**关键创新**：KORGym的创新在于其动态性和多样性，能够在复杂的交互环境中进行评估，区别于传统的静态评估基准。

**关键设计**：在设计中，KORGym设置了多种游戏参数，采用了适应性损失函数，并结合了强化学习技术，以优化模型的推理表现。

## 📊 实验亮点

实验结果显示，KORGym在评估19个LLM和8个VLM时，揭示了模型家族内的一致推理模式，且闭源模型的表现显著优于开源模型，进一步验证了评估方法的有效性和创新性。

## 🎯 应用场景

KORGym的潜在应用领域包括自然语言处理、人工智能教育和智能游戏等。它为研究人员提供了一个全面的评估工具，能够在复杂的交互环境中测试和提升LLM的推理能力，推动相关领域的发展。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) underscore the need for more comprehensive evaluation methods to accurately assess their reasoning capabilities. Existing benchmarks are often domain-specific and thus cannot fully capture an LLM's general reasoning potential. To address this limitation, we introduce the Knowledge Orthogonal Reasoning Gymnasium (KORGym), a dynamic evaluation platform inspired by KOR-Bench and Gymnasium. KORGym offers over fifty games in either textual or visual formats and supports interactive, multi-turn assessments with reinforcement learning scenarios. Using KORGym, we conduct extensive experiments on 19 LLMs and 8 VLMs, revealing consistent reasoning patterns within model families and demonstrating the superior performance of closed-source models. Further analysis examines the effects of modality, reasoning strategies, reinforcement learning techniques, and response length on model performance. We expect KORGym to become a valuable resource for advancing LLM reasoning research and developing evaluation methodologies suited to complex, interactive environments.


---
layout: default
title: "SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs via Stable Safety-critical Expert Identification"
---

# SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs via Stable Safety-critical Expert Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17368" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17368v2</a>
  <a href="https://arxiv.org/pdf/2506.17368.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17368v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17368v2', 'SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs via Stable Safety-critical Expert Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenglin Lai, Mengyao Liao, Bingzhe Wu, Dong Xu, Zebin Zhao, Zhihang Yuan, Chao Fan, Jianqiang Li

**分类**: cs.LG, cs.AI, cs.CR

**发布日期**: 2025-06-20 (更新: 2025-10-12)

**备注**: 10 pages, 8 figures

---

## 💡 一句话要点

**提出SAFEx以解决MoE架构LLMs的安全对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `安全对齐` `大型语言模型` `专家选择` `对抗性输入` `安全干预` `模型优化`

## 📋 核心要点

1. 现有的密集模型技术无法有效应对MoE架构中路由机制带来的安全对齐挑战，导致安全风险增加。
2. SAFEx框架通过稳定性基础的专家选择程序，识别和验证安全关键专家，分为HCDG和HRCG两组以应对安全问题。
3. 在Qwen3-30B-A3B模型上，禁用12个专家后拒绝率降低22%，并通过LoRA轻量适应实现了在对抗性提示下的安全响应改进。

## 📝 摘要（中文）

混合专家（MoE）架构的大型语言模型在效率和可扩展性方面表现出色，但其路由机制引入的安全对齐挑战尚未得到充分解决。本文正式化并系统分析了MoE特有的安全风险，即安全对齐行为依赖于特定专家模块。提出了SAFEx分析框架，通过基于稳定性的专家选择程序，稳健地识别、表征和验证安全关键专家，并将其分解为有害内容检测组（HCDG）和有害响应控制组（HRCG）。通过对SAFEx选择的专家进行目标掩蔽，发现安全行为高度集中。实验结果表明，禁用12个选定专家可将拒绝率降低22%。

## 🔬 方法详解

**问题定义**：本文解决的是MoE架构中安全对齐不足的问题，现有方法未能有效识别和控制安全关键专家，导致安全风险集中在特定模块上。

**核心思路**：提出SAFEx框架，通过稳定性基础的专家选择程序，识别和验证安全关键专家，进而分解为HCDG和HRCG，以实现更有效的安全干预。

**技术框架**：SAFEx框架包括专家选择、专家表征和验证三个主要模块，首先通过稳定性分析选择专家，然后对其进行功能分组，最后进行干预测试以验证效果。

**关键创新**：SAFEx的创新在于针对MoE架构的安全风险进行系统分析，首次明确了安全行为的集中性，并提出了基于专家的干预方法。

**关键设计**：在实验中，使用了48个MoE-FFN层和每层128个专家的配置，采用top-8路由，禁用特定专家后通过负权重合并进行轻量适应，优化了安全响应。

## 📊 实验亮点

实验结果显示，在Qwen3-30B-A3B模型上，禁用12个SAFEx选择的专家后，拒绝率降低了22%。此外，通过LoRA轻量适应，针对HRCG的负权重合并显著提升了在对抗性提示下的安全响应，展示了SAFEx的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性提升、智能助手的安全响应机制以及对抗性输入的处理。通过有效识别和控制安全关键专家，SAFEx为模型的安全性提供了一种计算高效的干预路径，未来可广泛应用于各类基于MoE架构的智能系统中。

## 📄 摘要（原文）

> Large language models with Mixture-of-Experts (MoE) architectures achieve efficiency and scalability, yet their routing mechanisms introduce safety alignment challenges insufficiently addressed by techniques developed for dense models. In this work, the MoE-specific safety risk of positional vulnerability-that safety-aligned behaviors rely on specific expert modules-is formalized and systematically analyzed. An analytical framework, SAFEx, is presented to robustly identify, characterize, and validate safety-critical experts via a stability-based expert selection procedure, and to decompose them into two functional groups: the Harmful Content Detection Group (HCDG), which specializes in identifying and recognizing harmful content within user inputs, and the Harmful Response Control Group (HRCG), which specializes in controlling and enforcing model behaviors to generate appropriate safety responses. Expert-level interventions are conducted to probe causality and to test mitigation. Targeted masking of SAFEx-selected experts reveals that safety behavior is highly concentrated. On Qwen3-30B-A3B, configured with 48 MoE-FFN layers and 128 experts per layer under top-8 routing (48x128=6,144 experts in total), disabling 12 selected experts reduces the refusal rate by 22%. In addition, lightweight adaptation is performed using LoRA under three configurations-the HRCG, the union of HCDG and HRCG, and all experts-and the resulting updates are composed through negative weight merging targeted at the HRCG, leading to improved refusal under adversarial prompts without full-model retraining. These results establish positional vulnerability as a distinct MoE-specific safety challenge and provide a practical, compute-efficient pathway for expert-level safety interventions within routed architectures.


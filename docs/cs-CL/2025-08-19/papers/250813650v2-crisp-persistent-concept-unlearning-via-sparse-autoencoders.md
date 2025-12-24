---
layout: default
title: "CRISP: Persistent Concept Unlearning via Sparse Autoencoders"
---

# CRISP: Persistent Concept Unlearning via Sparse Autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13650" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13650v2</a>
  <a href="https://arxiv.org/pdf/2508.13650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13650v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13650v2', 'CRISP: Persistent Concept Unlearning via Sparse Autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tomer Ashuach, Dana Arad, Aaron Mueller, Martin Tutek, Yonatan Belinkov

**分类**: cs.CL

**发布日期**: 2025-08-19 (更新: 2025-11-20)

**备注**: 18 pages, 5 figures

---

## 💡 一句话要点

**提出CRISP以解决大语言模型知识去除问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `知识去除` `大型语言模型` `安全性` `特征抑制`

## 📋 核心要点

1. 现有基于稀疏自编码器的方法在推理时进行干预，无法实现模型参数的持久性变化，易被恶意行为者绕过。
2. CRISP通过自动识别多个层中的显著特征并抑制其激活，提供了一种高效的持久概念去除方案。
3. 在WMDP基准测试中，CRISP在安全关键去除任务上表现优异，成功去除了有害知识，同时保持了模型的整体能力。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在实际应用中的广泛部署，选择性去除不必要知识的需求变得尤为重要。近期研究利用稀疏自编码器（SAEs）对单义特征进行精确干预，但大多数SAE方法仅在推理时操作，无法在模型参数中实现持久性变化。本文提出CRISP，一种基于SAEs的参数高效的持久概念去除方法。CRISP自动识别多个层中的显著SAE特征并抑制其激活。实验表明，该方法在WMDP基准的安全关键去除任务中优于以往方法，成功去除有害知识，同时保留一般和领域内能力。特征级分析显示，CRISP实现了目标与良性概念之间的语义一致分离，允许精确抑制目标特征。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中不必要知识的去除问题。现有方法多在推理阶段进行干预，无法实现持久性效果，且易被恶意攻击者逆转。

**核心思路**：CRISP的核心思想是利用稀疏自编码器自动识别和抑制多个层中的显著特征，从而实现持久的概念去除。该设计旨在确保模型在去除有害知识的同时，保留其有效性和功能。

**技术框架**：CRISP的整体架构包括特征识别模块和激活抑制模块。特征识别模块通过分析模型的多个层，识别出需要去除的显著特征；激活抑制模块则负责降低这些特征的激活水平。

**关键创新**：CRISP的主要创新在于其能够在多个层次上实现特征的持久性去除，而非仅限于推理阶段的临时干预。这一方法显著提高了去除效果的稳定性和安全性。

**关键设计**：在参数设置上，CRISP采用了特定的损失函数来优化特征抑制效果，同时在网络结构上结合了多层稀疏自编码器，以确保特征的有效识别与抑制。具体的参数和结构设计细节在实验部分进行了详细描述。

## 📊 实验亮点

在WMDP基准测试中，CRISP在安全关键去除任务上表现优异，相较于以往方法，成功去除了有害知识，同时保持了模型的整体能力，具体提升幅度未明确说明，但实验结果显示其在特征级别上实现了更为精确的抑制。

## 🎯 应用场景

CRISP的研究成果在多个领域具有潜在应用价值，尤其是在需要对大型语言模型进行知识管理和安全控制的场景中，如金融、医疗和法律等安全关键领域。通过有效去除有害知识，CRISP能够提升模型的安全性和可靠性，减少潜在的风险和误用。未来，该方法可能会推动更多关于模型知识去除的研究与应用。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly deployed in real-world applications, the need to selectively remove unwanted knowledge while preserving model utility has become paramount. Recent work has explored sparse autoencoders (SAEs) to perform precise interventions on monosemantic features. However, most SAE-based methods operate at inference time, which does not create persistent changes in the model's parameters. Such interventions can be bypassed or reversed by malicious actors with parameter access. We introduce CRISP, a parameter-efficient method for persistent concept unlearning using SAEs. CRISP automatically identifies salient SAE features across multiple layers and suppresses their activations. We experiment with two LLMs and show that our method outperforms prior approaches on safety-critical unlearning tasks from the WMDP benchmark, successfully removing harmful knowledge while preserving general and in-domain capabilities. Feature-level analysis reveals that CRISP achieves semantically coherent separation between target and benign concepts, allowing precise suppression of the target features.


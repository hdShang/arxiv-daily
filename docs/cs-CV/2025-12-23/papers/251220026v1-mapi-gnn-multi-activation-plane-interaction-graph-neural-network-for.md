---
layout: default
title: MAPI-GNN: Multi-Activation Plane Interaction Graph Neural Network for Multimodal Medical Diagnosis
---

# MAPI-GNN: Multi-Activation Plane Interaction Graph Neural Network for Multimodal Medical Diagnosis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20026" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20026v1</a>
  <a href="https://arxiv.org/pdf/2512.20026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20026v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20026v1', 'MAPI-GNN: Multi-Activation Plane Interaction Graph Neural Network for Multimodal Medical Diagnosis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziwei Qin, Xuhui Song, Deqing Huang, Na Qin, Jun Li

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Accepted by Proceedings of the AAAI Conference on Artificial Intelligence 40 (AAAI-26)

---

## 💡 一句话要点

**MAPI-GNN：用于多模态医学诊断的多激活平面交互图神经网络**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态医学诊断` `图神经网络` `多激活平面` `特征解耦` `关系建模`

## 📋 核心要点

1. 现有GNN方法在多模态医学诊断中依赖单一静态图，无法有效建模患者个体化的病理关系。
2. MAPI-GNN通过学习语义解耦的特征子空间，动态构建多激活平面图，从而捕捉更丰富的病理关系。
3. 在两个医学诊断任务上的实验表明，MAPI-GNN显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

图神经网络（GNN）因其固有的关系建模能力，越来越多地应用于多模态医学诊断。然而，由于过度依赖从无差别特征构建的单一静态图，GNN的有效性常常受到影响，从而阻碍了对患者特定病理关系的建模。为此，本文提出了多激活平面交互图神经网络（MAPI-GNN），通过从语义上解耦的特征子空间学习多方面的图谱来重构这种单图范式。该框架首先通过多维判别器发现潜在的图感知模式；然后，这些模式指导动态构建一系列激活图；最后，通过关系融合引擎对这种多方面的图谱进行聚合和上下文感知，从而实现稳健的诊断。在包含超过1300个患者样本的两个不同任务上进行的大量实验表明，MAPI-GNN显著优于最先进的方法。

## 🔬 方法详解

**问题定义**：现有的多模态医学诊断方法，特别是基于图神经网络的方法，通常使用单一的、静态的图结构来表示患者的特征关系。这种方法忽略了不同模态特征之间的复杂交互，以及患者个体差异导致的病理关系变化，限制了诊断的准确性。痛点在于无法有效建模患者特异性的病理关系。

**核心思路**：MAPI-GNN的核心思路是从语义解耦的特征子空间中学习多方面的图谱，即构建多个“激活平面图”。每个激活平面图捕捉不同语义下的特征关系，从而更全面地表示患者的病理信息。通过动态构建和融合这些激活平面图，可以更好地建模患者个体化的病理关系。

**技术框架**：MAPI-GNN框架主要包含三个阶段：1) **多维判别器**：用于发现潜在的图感知模式，即学习不同语义下的特征子空间。2) **动态激活图构建**：基于判别器学习到的模式，动态构建一系列激活图，每个图对应一个特征子空间。3) **关系融合引擎**：将多个激活图进行聚合和上下文感知，最终用于诊断。

**关键创新**：MAPI-GNN的关键创新在于引入了多激活平面图的概念，打破了传统GNN方法中单一图的限制。通过从语义解耦的特征子空间学习多个图，可以更全面地捕捉患者的病理信息，从而提高诊断的准确性。与现有方法的本质区别在于，MAPI-GNN能够动态地学习和融合多个图结构，而现有方法通常使用预定义的或静态的图结构。

**关键设计**：多维判别器的具体实现方式未知，但推测可能使用了某种形式的注意力机制或自编码器来学习特征子空间。激活图的构建方式可能是基于特征相似性或相关性。关系融合引擎可能使用了图卷积网络或注意力机制来聚合和上下文感知多个激活图的信息。损失函数的设计可能包括诊断分类损失和某种正则化项，以鼓励学习到更具区分性的特征子空间。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20026v1/fig2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20026v1/fig3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20026v1/fig4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MAPI-GNN在两个不同的多模态医学诊断任务上进行了评估，实验结果表明，MAPI-GNN显著优于现有的最先进方法。具体性能数据和提升幅度未知，但摘要中强调了“显著优于最先进的方法”，表明MAPI-GNN在诊断准确性方面取得了重要突破。

## 🎯 应用场景

MAPI-GNN在多模态医学诊断领域具有广泛的应用前景，例如疾病预测、风险评估、个性化治疗方案制定等。通过整合影像、基因、临床数据等多模态信息，MAPI-GNN能够更准确地识别疾病特征，提高诊断效率，并为患者提供更精准的医疗服务。未来，该方法有望应用于更广泛的医学领域，助力实现智能化医疗。

## 📄 摘要（原文）

> Graph neural networks are increasingly applied to multimodal medical diagnosis for their inherent relational modeling capabilities. However, their efficacy is often compromised by the prevailing reliance on a single, static graph built from indiscriminate features, hindering the ability to model patient-specific pathological relationships. To this end, the proposed Multi-Activation Plane Interaction Graph Neural Network (MAPI-GNN) reconstructs this single-graph paradigm by learning a multifaceted graph profile from semantically disentangled feature subspaces. The framework first uncovers latent graph-aware patterns via a multi-dimensional discriminator; these patterns then guide the dynamic construction of a stack of activation graphs; and this multifaceted profile is finally aggregated and contextualized by a relational fusion engine for a robust diagnosis. Extensive experiments on two diverse tasks, comprising over 1300 patient samples, demonstrate that MAPI-GNN significantly outperforms state-of-the-art methods.


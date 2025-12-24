---
layout: default
title: Adversarial Attacks against Closed-Source MLLMs via Feature Optimal Alignment
---

# Adversarial Attacks against Closed-Source MLLMs via Feature Optimal Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21494" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21494v1</a>
  <a href="https://arxiv.org/pdf/2505.21494.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21494v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21494v1', 'Adversarial Attacks against Closed-Source MLLMs via Feature Optimal Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojun Jia, Sensen Gao, Simeng Qin, Tianyu Pang, Chao Du, Yihao Huang, Xinfeng Li, Yiming Li, Bo Li, Yang Liu

**分类**: cs.CV

**发布日期**: 2025-05-27

**🔗 代码/项目**: [GITHUB](https://github.com/jiaxiaojunQAQ/FOA-Attack)

---

## 💡 一句话要点

**提出FOA-Attack以解决闭源MLLMs的对抗攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `多模态大型语言模型` `特征对齐` `最优传输` `聚类技术` `模型鲁棒性` `安全性测试`

## 📋 核心要点

1. 现有方法在对抗攻击中主要依赖全局特征对齐，忽视了局部信息，导致转移性不足。
2. 本文提出FOA-Attack，通过全局特征损失和局部聚类最优传输损失实现对抗样本的有效对齐。
3. 实验结果显示，FOA-Attack在多个模型上超越了当前最先进的方法，尤其在闭源MLLMs上表现显著提升。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）仍然容易受到可转移的对抗样本攻击。现有方法通常通过对齐全局特征（如CLIP的[CLS]标记）来实现针对性攻击，但往往忽视了补丁标记中编码的丰富局部信息。这导致对齐效果不佳和转移性有限，尤其是在闭源模型中。为了解决这一限制，本文提出了一种基于特征最优对齐的针对性可转移对抗攻击方法FOA-Attack，以提高对抗转移能力。我们在全局层面引入基于余弦相似度的全局特征损失，以对齐对抗样本与目标样本的粗粒度特征；在局部层面，利用聚类技术提取紧凑的局部模式，缓解冗余局部特征。我们将对抗样本与目标样本之间的局部特征对齐形式化为最优传输（OT）问题，并提出局部聚类最优传输损失以优化细粒度特征对齐。实验结果表明，该方法在多个模型上优于现有最先进方法，尤其是在转移到闭源MLLMs时表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型（MLLMs）在对抗攻击中的脆弱性，现有方法主要依赖全局特征对齐，忽视了局部特征的丰富信息，导致对抗样本的转移性不足，尤其是在闭源模型中。

**核心思路**：FOA-Attack的核心思路是通过全局特征损失和局部聚类最优传输损失来优化对抗样本与目标样本之间的特征对齐，从而提高对抗样本的转移能力。全局层面使用余弦相似度对齐粗粒度特征，局部层面则通过聚类提取紧凑的局部模式。

**技术框架**：FOA-Attack的整体架构包括全局特征对齐模块和局部特征对齐模块。全局模块通过计算对抗样本与目标样本的余弦相似度来优化特征对齐，而局部模块则利用聚类技术和最优传输理论来处理细粒度特征的对齐。

**关键创新**：本文的关键创新在于引入了局部聚类最优传输损失，这一方法有效地解决了现有方法中对局部特征对齐不足的问题，显著提升了对抗样本的转移性。

**关键设计**：在损失函数设计上，采用了全局特征损失和局部聚类最优传输损失，动态集成模型加权策略用于平衡多个模型的影响，进一步提高了对抗样本生成的效果。

## 📊 实验亮点

实验结果表明，FOA-Attack在多个闭源MLLMs上表现优越，相较于现有最先进的方法，转移率提升了显著，具体性能数据未详述，但实验显示其在对抗样本生成方面的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、对抗样本生成和模型鲁棒性评估等。FOA-Attack可以帮助研究人员和开发者更好地理解和应对多模态大型语言模型的安全风险，提升模型在实际应用中的可靠性和安全性。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) remain vulnerable to transferable adversarial examples. While existing methods typically achieve targeted attacks by aligning global features-such as CLIP's [CLS] token-between adversarial and target samples, they often overlook the rich local information encoded in patch tokens. This leads to suboptimal alignment and limited transferability, particularly for closed-source models. To address this limitation, we propose a targeted transferable adversarial attack method based on feature optimal alignment, called FOA-Attack, to improve adversarial transfer capability. Specifically, at the global level, we introduce a global feature loss based on cosine similarity to align the coarse-grained features of adversarial samples with those of target samples. At the local level, given the rich local representations within Transformers, we leverage clustering techniques to extract compact local patterns to alleviate redundant local features. We then formulate local feature alignment between adversarial and target samples as an optimal transport (OT) problem and propose a local clustering optimal transport loss to refine fine-grained feature alignment. Additionally, we propose a dynamic ensemble model weighting strategy to adaptively balance the influence of multiple models during adversarial example generation, thereby further improving transferability. Extensive experiments across various models demonstrate the superiority of the proposed method, outperforming state-of-the-art methods, especially in transferring to closed-source MLLMs. The code is released at https://github.com/jiaxiaojunQAQ/FOA-Attack.


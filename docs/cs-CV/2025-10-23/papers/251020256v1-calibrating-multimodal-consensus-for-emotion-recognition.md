---
layout: default
title: Calibrating Multimodal Consensus for Emotion Recognition
---

# Calibrating Multimodal Consensus for Emotion Recognition

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20256" target="_blank" class="toolbar-btn">arXiv: 2510.20256v1</a>
    <a href="https://arxiv.org/pdf/2510.20256.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20256v1" 
            onclick="toggleFavorite(this, '2510.20256v1', 'Calibrating Multimodal Consensus for Emotion Recognition')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guowei Zhong, Junjie Li, Huaiyu Zhu, Ruohong Huan, Yun Pan

**分类**: cs.CV, cs.CL, cs.LG, cs.MM

**发布日期**: 2025-10-23

**🔗 代码/项目**: [GITHUB](https://github.com/gw-zhong/CMC)

---

## 💡 一句话要点

**提出校准多模态共识模型以解决情感识别中的语义不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感识别` `伪标签生成` `无参数融合` `语义一致性` `情感分析`

## 📋 核心要点

1. 现有多模态情感识别方法忽视了模态间的语义不一致性，导致情感线索冲突，影响识别准确性。
2. 提出的校准多模态共识模型通过伪标签生成和无参数融合模块，减轻文本模态的主导地位，提升融合效果。
3. 实验结果显示，CMC在多个数据集上表现优越，尤其在存在语义不一致的场景中，识别性能显著提升。

## 📝 摘要（中文）

近年来，多模态情感识别（MER）取得了显著进展。然而，大多数现有方法忽视了不同模态之间可能出现的语义不一致性，例如文本和视觉输入之间的情感线索冲突。此外，当前方法往往受到文本模态的主导影响，导致识别准确性下降。为了解决这些挑战，本文提出了一种名为校准多模态共识（CMC）的模型。CMC引入了伪标签生成模块（PLGM），以自监督方式生成伪单模态标签，从而实现单模态预训练。接着，采用无参数融合模块（PFM）和多模态共识路由器（MCR）进行多模态微调，减轻文本主导性并引导融合过程朝向更可靠的共识。实验结果表明，CMC在四个数据集（CH-SIMS、CH-SIMS v2、CMU-MOSI和CMU-MOSEI）上的表现与最先进的方法相当或更优，并在CH-SIMS和CH-SIMS v2上表现出显著优势。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态情感识别中模态间语义不一致性的问题，现有方法往往受到文本模态的主导影响，导致情感识别准确性下降。

**核心思路**：提出的校准多模态共识模型（CMC）通过伪标签生成模块（PLGM）实现自监督的单模态预训练，进而通过无参数融合模块（PFM）和多模态共识路由器（MCR）进行有效的多模态微调，以减轻文本模态的主导性。

**技术框架**：CMC模型主要包括三个模块：伪标签生成模块（PLGM）用于生成伪单模态标签，促进单模态的自监督学习；无参数融合模块（PFM）用于融合不同模态的信息；多模态共识路由器（MCR）则负责引导融合过程，确保最终的情感识别结果更为可靠。

**关键创新**：CMC的核心创新在于引入伪标签生成机制和无参数融合策略，这与现有方法的单一模态主导性形成鲜明对比，能够有效缓解模态间的语义冲突。

**关键设计**：在模型设计中，PLGM通过自监督学习生成伪标签，PFM则采用无参数设计以简化融合过程，MCR通过动态调整模态权重来优化最终的情感识别结果。

## 📊 实验亮点

实验结果表明，CMC在CH-SIMS、CH-SIMS v2、CMU-MOSI和CMU-MOSEI四个数据集上表现优越，尤其在CH-SIMS和CH-SIMS v2数据集中，针对语义不一致场景的识别性能显著提升，达到了最先进方法的水平或更优。

## 🎯 应用场景

该研究在情感分析、社交媒体监测、心理健康评估等领域具有广泛的应用潜力。通过提高多模态情感识别的准确性，能够更好地理解用户情感，进而为个性化服务和干预措施提供支持。未来，该模型还可以扩展到其他多模态任务，如情感驱动的对话系统和情感智能机器人等。

## 📄 摘要（原文）

> In recent years, Multimodal Emotion Recognition (MER) has made substantial progress. Nevertheless, most existing approaches neglect the semantic inconsistencies that may arise across modalities, such as conflicting emotional cues between text and visual inputs. Besides, current methods are often dominated by the text modality due to its strong representational capacity, which can compromise recognition accuracy. To address these challenges, we propose a model termed Calibrated Multimodal Consensus (CMC). CMC introduces a Pseudo Label Generation Module (PLGM) to produce pseudo unimodal labels, enabling unimodal pretraining in a self-supervised fashion. It then employs a Parameter-free Fusion Module (PFM) and a Multimodal Consensus Router (MCR) for multimodal finetuning, thereby mitigating text dominance and guiding the fusion process toward a more reliable consensus. Experimental results demonstrate that CMC achieves performance on par with or superior to state-of-the-art methods across four datasets, CH-SIMS, CH-SIMS v2, CMU-MOSI, and CMU-MOSEI, and exhibits notable advantages in scenarios with semantic inconsistencies on CH-SIMS and CH-SIMS v2. The implementation of this work is publicly accessible at https://github.com/gw-zhong/CMC.


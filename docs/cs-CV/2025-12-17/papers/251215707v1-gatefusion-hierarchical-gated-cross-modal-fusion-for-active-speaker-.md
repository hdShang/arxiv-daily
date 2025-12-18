---
layout: default
title: GateFusion: Hierarchical Gated Cross-Modal Fusion for Active Speaker Detection
---

# GateFusion: Hierarchical Gated Cross-Modal Fusion for Active Speaker Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15707" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15707v1</a>
  <a href="https://arxiv.org/pdf/2512.15707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15707v1" onclick="toggleFavorite(this, '2512.15707v1', 'GateFusion: Hierarchical Gated Cross-Modal Fusion for Active Speaker Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Wang, Juhyung Ha, Frangil M. Ramirez, Yuchen Wang, David J. Crandall

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: accepted by WACV 2026

---

## 💡 一句话要点

**提出GateFusion，通过分层门控跨模态融合提升主动说话人检测性能**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `主动说话人检测` `多模态融合` `分层门控` `Transformer` `跨模态学习` `视频分析` `音频分析`

## 📋 核心要点

1. 现有主动说话人检测方法依赖后期融合，无法有效捕捉细粒度的跨模态交互，导致在复杂场景下性能受限。
2. GateFusion通过分层门控融合解码器HiGate，在Transformer多层自适应地融合视觉和音频特征，实现更有效的跨模态信息交互。
3. 实验表明，GateFusion在多个基准测试上显著提升了主动说话人检测的性能，并在领域外数据上表现出良好的泛化能力。

## 📝 摘要（中文）

主动说话人检测（ASD）旨在识别视频中每一帧的说话人。现有方法主要依赖于后期融合，但这种方式难以捕捉细粒度的跨模态交互，这对于复杂场景下的鲁棒性至关重要。本文提出GateFusion，一种结合了强大的预训练单模态编码器和分层门控融合解码器（HiGate）的新架构。HiGate通过可学习的双模态条件门控，自适应地将一种模态的上下文特征注入到Transformer骨干网络的多个层中，实现渐进式的多深度融合。为了进一步加强多模态学习，我们提出了两个辅助目标：掩码对齐损失（MAL），用于对齐单模态输出与多模态预测；过正惩罚（OPP），用于抑制虚假的仅视频激活。GateFusion在多个具有挑战性的ASD基准测试上取得了新的state-of-the-art结果，在Ego4D-ASD、UniTalk和WASD基准测试上分别实现了77.8% mAP (+9.4%)、86.1% mAP (+2.9%)和96.1% mAP (+0.5%)，并在AVA-ActiveSpeaker上实现了有竞争力的性能。领域外实验证明了我们模型的泛化能力，而全面的消融实验表明了每个组件的互补优势。

## 🔬 方法详解

**问题定义**：主动说话人检测旨在确定视频中每一帧的说话人。现有方法，特别是基于后期融合的方法，无法充分利用视觉和音频之间的细粒度交互信息，导致在复杂、噪声大的环境中性能下降。这些方法难以区分仅通过视觉或音频线索无法明确判断的说话人。

**核心思路**：GateFusion的核心思想是在Transformer架构的多个层级上，通过门控机制控制不同模态信息的融合程度。这种分层融合允许模型逐步学习跨模态的关联性，并根据上下文信息自适应地调整各模态的贡献，从而更有效地利用多模态信息。

**技术框架**：GateFusion主要包含三个部分：预训练的单模态编码器（用于提取视觉和音频特征）、分层门控融合解码器（HiGate）以及辅助损失函数。视觉和音频数据分别通过各自的编码器提取特征，然后输入到HiGate中进行融合。HiGate在Transformer的每一层都使用门控机制来控制视觉和音频特征的融合比例。最后，通过辅助损失函数（MAL和OPP）来进一步优化模型的学习。

**关键创新**：GateFusion的关键创新在于HiGate，它是一种分层的、门控的跨模态融合机制。与传统的后期融合方法不同，HiGate允许在Transformer的多个层级上进行特征融合，从而能够捕捉更细粒度的跨模态交互。此外，门控机制允许模型根据上下文信息自适应地调整各模态的贡献，从而提高模型的鲁棒性。

**关键设计**：HiGate使用可学习的双模态条件门控来控制视觉和音频特征的融合比例。掩码对齐损失（MAL）通过最小化单模态输出与多模态预测之间的差异来促进模态对齐。过正惩罚（OPP）通过惩罚仅视频激活来抑制虚假的检测结果。具体实现细节包括Transformer的层数、门控机制的类型、损失函数的权重等。这些参数需要根据具体任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15707v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15707v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15707v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GateFusion在Ego4D-ASD、UniTalk和WASD等多个具有挑战性的主动说话人检测基准测试上取得了显著的性能提升，mAP分别提升了9.4%、2.9%和0.5%，达到了state-of-the-art水平。消融实验表明，HiGate、MAL和OPP等组件都对性能提升有贡献，证明了GateFusion架构的有效性。

## 🎯 应用场景

GateFusion在视频会议、人机交互、监控系统等领域具有广泛的应用前景。它可以用于自动识别视频中的发言者，提高会议记录的效率，改善人机交互的自然性，并增强监控系统的智能分析能力。未来，该技术可以进一步扩展到其他多模态任务，如视频摘要、情感识别等。

## 📄 摘要（原文）

> Active Speaker Detection (ASD) aims to identify who is currently speaking in each frame of a video. Most state-of-the-art approaches rely on late fusion to combine visual and audio features, but late fusion often fails to capture fine-grained cross-modal interactions, which can be critical for robust performance in unconstrained scenarios. In this paper, we introduce GateFusion, a novel architecture that combines strong pretrained unimodal encoders with a Hierarchical Gated Fusion Decoder (HiGate). HiGate enables progressive, multi-depth fusion by adaptively injecting contextual features from one modality into the other at multiple layers of the Transformer backbone, guided by learnable, bimodally-conditioned gates. To further strengthen multimodal learning, we propose two auxiliary objectives: Masked Alignment Loss (MAL) to align unimodal outputs with multimodal predictions, and Over-Positive Penalty (OPP) to suppress spurious video-only activations. GateFusion establishes new state-of-the-art results on several challenging ASD benchmarks, achieving 77.8% mAP (+9.4%), 86.1% mAP (+2.9%), and 96.1% mAP (+0.5%) on Ego4D-ASD, UniTalk, and WASD benchmarks, respectively, and delivering competitive performance on AVA-ActiveSpeaker. Out-of-domain experiments demonstrate the generalization of our model, while comprehensive ablations show the complementary benefits of each component.


---
layout: default
title: Complementary and Contrastive Learning for Audio-Visual Segmentation
---

# Complementary and Contrastive Learning for Audio-Visual Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10051" target="_blank" class="toolbar-btn">arXiv: 2510.10051v1</a>
    <a href="https://arxiv.org/pdf/2510.10051.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10051v1" 
            onclick="toggleFavorite(this, '2510.10051v1', 'Complementary and Contrastive Learning for Audio-Visual Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sitong Gong, Yunzhi Zhuge, Lu Zhang, Pingping Zhang, Huchuan Lu

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: Accepted to IEEE Transactions on Multimedia

**🔗 代码/项目**: [GITHUB](https://github.com/SitongGong/CCFormer)

---

## 💡 一句话要点

**提出CCFormer，通过互补对比学习实现更精准的音视频分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频分割` `跨模态学习` `Transformer` `对比学习` `时空建模` `多模态融合` `深度学习`

## 📋 核心要点

1. 现有音视频分割方法难以充分提取多模态系数和时间动态，限制了分割精度和鲁棒性。
2. CCFormer通过早期集成、多查询Transformer和双模态对比学习，全面捕获时空上下文信息。
3. 实验结果表明，CCFormer在S4、MS3和AVSS数据集上均取得了state-of-the-art的性能。

## 📝 摘要（中文）

音视频分割(AVS)旨在生成与物体声音信号相关的像素级分割图。该领域涌现了大量基于CNN和Transformer的方法，显著提升了分割精度和鲁棒性。传统CNN方法通过填充和乘法等基本操作管理音视频交互，但受限于CNN局部感受野。Transformer方法将音频线索作为查询，利用注意力机制增强帧内音视频协作，但通常难以充分提取多模态系数和时间动态。为克服这些限制，我们提出了互补对比Transformer(CCFormer)，一个擅长处理局部和全局信息并全面捕获时空上下文的新框架。CCFormer首先使用早期集成模块(EIM)，采用并行双边架构，将多尺度视觉特征与音频数据融合，以增强跨模态互补性。为了提取帧内空间特征并促进时间连贯性的感知，我们引入了多查询Transformer模块(MTM)，该模块动态地赋予音频查询学习能力，并同时建模帧和视频级别的关系。此外，我们提出了双模态对比学习(BCL)来促进统一特征空间中两种模态的对齐。通过有效结合这些设计，我们的方法在S4、MS3和AVSS数据集上建立了新的state-of-the-art基准。

## 🔬 方法详解

**问题定义**：音视频分割(AVS)旨在根据给定的音视频信息，对视频中的目标物体进行像素级别的分割。现有方法，特别是基于CNN和Transformer的方法，在处理跨模态信息融合和时序信息建模方面存在不足，导致分割精度受限。CNN方法感受野有限，Transformer方法难以有效提取多模态系数和时间动态。

**核心思路**：CCFormer的核心思路是利用互补学习和对比学习，充分挖掘音视频之间的关联性和差异性。通过早期集成模块(EIM)增强跨模态互补性，多查询Transformer模块(MTM)提取帧内空间特征和时间连贯性，双模态对比学习(BCL)促进模态对齐，从而实现更精准的音视频分割。

**技术框架**：CCFormer主要包含三个模块：早期集成模块(EIM)、多查询Transformer模块(MTM)和双模态对比学习(BCL)。EIM负责融合多尺度视觉特征和音频数据；MTM利用多查询Transformer动态学习音频查询，建模帧和视频级别的关系；BCL通过对比学习促进音视频特征在统一特征空间的对齐。整体流程是先通过EIM进行初步融合，再通过MTM提取时空特征，最后通过BCL进行特征对齐和优化。

**关键创新**：CCFormer的关键创新在于三个方面：一是并行双边架构的早期集成模块，有效融合多尺度视觉特征和音频数据；二是多查询Transformer模块，动态学习音频查询并建模时序关系；三是双模态对比学习，促进音视频特征在统一特征空间的对齐。与现有方法相比，CCFormer更全面地考虑了跨模态信息融合和时序信息建模，从而提升了分割精度。

**关键设计**：EIM采用并行双边架构，分别处理视觉和音频信息，并通过跨模态注意力机制进行融合。MTM使用多个查询头，每个查询头负责学习不同的音频特征，从而更全面地捕捉音频信息。BCL使用InfoNCE损失函数，最大化正样本对的相似度，最小化负样本对的相似度，从而促进音视频特征的对齐。

## 📊 实验亮点

CCFormer在S4、MS3和AVSS三个音视频分割数据集上均取得了state-of-the-art的性能。例如，在S4数据集上，CCFormer的mIoU指标相比现有最佳方法提升了显著幅度。实验结果充分验证了CCFormer在跨模态信息融合和时序信息建模方面的优势，以及互补对比学习的有效性。

## 🎯 应用场景

CCFormer在音视频分割领域具有广泛的应用前景，例如视频监控、智能安防、自动驾驶、视频编辑等。通过精准的音视频分割，可以实现对特定声音事件相关物体的自动识别和跟踪，从而提升系统的智能化水平和用户体验。未来，该技术还可以应用于虚拟现实、增强现实等领域，实现更沉浸式的音视频互动体验。

## 📄 摘要（原文）

> Audio-Visual Segmentation (AVS) aims to generate pixel-wise segmentation maps that correlate with the auditory signals of objects. This field has seen significant progress with numerous CNN and Transformer-based methods enhancing the segmentation accuracy and robustness. Traditional CNN approaches manage audio-visual interactions through basic operations like padding and multiplications but are restricted by CNNs' limited local receptive field. More recently, Transformer-based methods treat auditory cues as queries, utilizing attention mechanisms to enhance audio-visual cooperation within frames. Nevertheless, they typically struggle to extract multimodal coefficients and temporal dynamics adequately. To overcome these limitations, we present the Complementary and Contrastive Transformer (CCFormer), a novel framework adept at processing both local and global information and capturing spatial-temporal context comprehensively. Our CCFormer initiates with the Early Integration Module (EIM) that employs a parallel bilateral architecture, merging multi-scale visual features with audio data to boost cross-modal complementarity. To extract the intra-frame spatial features and facilitate the perception of temporal coherence, we introduce the Multi-query Transformer Module (MTM), which dynamically endows audio queries with learning capabilities and models the frame and video-level relations simultaneously. Furthermore, we propose the Bi-modal Contrastive Learning (BCL) to promote the alignment across both modalities in the unified feature space. Through the effective combination of those designs, our method sets new state-of-the-art benchmarks across the S4, MS3 and AVSS datasets. Our source code and model weights will be made publicly available at https://github.com/SitongGong/CCFormer


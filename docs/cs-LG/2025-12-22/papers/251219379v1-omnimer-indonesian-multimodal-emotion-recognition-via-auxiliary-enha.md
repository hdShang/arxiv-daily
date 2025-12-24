---
layout: default
title: "OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation"
---

# OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19379" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19379v1</a>
  <a href="https://arxiv.org/pdf/2512.19379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19379v1', 'OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueming Yan, Boyan Xu, Yaochu Jin, Lixian Xiao, Wenlong Ye, Runyang Cai, Zeqi Zheng, Jingfa Liu, Aimin Yang

**分类**: cs.LG, cs.AI, cs.MM

**发布日期**: 2025-12-22

**🔗 代码/项目**: [GITHUB](https://github.com/yanxm01/INDOMER)

---

## 💡 一句话要点

**提出OmniMER以解决印尼多模态情感识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感识别` `印尼语` `情感计算` `辅助任务` `跨模态融合` `数据集构建` `深度学习`

## 📋 核心要点

1. 印尼语在多模态情感识别研究中服务不足，面临跨模态不一致性和长尾类分布等挑战。
2. 提出OmniMER框架，通过情感关键词提取、面部表情分析和音频韵律分析等辅助任务增强情感识别能力。
3. 实验结果显示，OmniMER在情感分类和识别上分别提升了7.6和22.1个绝对点，验证了其有效性。

## 📝 摘要（中文）

印尼语作为一种有超过2亿使用者的语言，在多模态情感识别研究中仍然处于服务不足的状态。我们引入了IndoMER，这是第一个针对印尼的多模态情感识别基准，包含来自203位说话者的1,944个视频片段，具有时间对齐的文本、音频和视觉注释，涵盖七种情感类别。该数据集展示了诸如跨模态不一致性和受印尼文化交流规范影响的长尾类分布等现实挑战。为了解决这些问题，我们提出了OmniMER，一个基于Qwen2.5-Omni的多模态适应框架，通过情感关键词提取、面部表情分析和音频韵律分析等三个辅助模态特定感知任务来增强情感识别。这些辅助任务帮助模型在融合前识别每种模态中的情感相关线索，从而减少在低资源环境下对虚假相关性的依赖。实验结果表明，OmniMER在情感分类和情感识别上分别达到了0.582和0.454的Macro-F1，较基线模型分别提升了7.6和22.1个绝对点。

## 🔬 方法详解

**问题定义**：本论文旨在解决印尼语多模态情感识别中的挑战，尤其是跨模态不一致性和长尾类分布的问题。现有方法在低资源环境下容易依赖虚假相关性，导致识别效果不佳。

**核心思路**：提出OmniMER框架，通过引入三个辅助模态特定感知任务，帮助模型在融合前识别情感相关线索，从而提高情感识别的准确性和鲁棒性。

**技术框架**：OmniMER框架基于Qwen2.5-Omni，包含三个主要模块：情感关键词提取、面部表情分析和音频韵律分析。每个模块分别处理文本、视频和音频数据，最终进行融合以实现情感识别。

**关键创新**：最重要的创新点在于通过辅助任务的设计，增强了模型对不同模态中情感线索的感知能力，显著减少了对虚假相关性的依赖。与现有方法相比，OmniMER在多模态融合中更具有效性和适应性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化每个辅助任务的输出，并通过调节超参数来平衡不同模态的影响，确保模型在多模态融合时的稳定性和准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19379v1/pdf/France.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19379v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19379v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，OmniMER在情感分类任务中达到了0.582的Macro-F1，在情感识别任务中达到了0.454，分别较基线模型提升了7.6和22.1个绝对点。此外，跨语言评估表明该框架具有良好的泛化能力。

## 🎯 应用场景

该研究在社交媒体分析、情感计算和人机交互等领域具有广泛的应用潜力。通过提升印尼语的情感识别能力，能够更好地理解和分析印尼文化中的情感表达，促进相关技术在东南亚地区的落地与发展。

## 📄 摘要（原文）

> Indonesian, spoken by over 200 million people, remains underserved in multimodal emotion recognition research despite its dominant presence on Southeast Asian social media platforms. We introduce IndoMER, the first multimodal emotion recognition benchmark for Indonesian, comprising 1,944 video segments from 203 speakers with temporally aligned text, audio, and visual annotations across seven emotion categories. The dataset exhibits realistic challenges including cross-modal inconsistency and long-tailed class distributions shaped by Indonesian cultural communication norms. To address these challenges, we propose OmniMER, a multimodal adaptation framework built upon Qwen2.5-Omni that enhances emotion recognition through three auxiliary modality-specific perception tasks: emotion keyword extraction for text, facial expression analysis for video, and prosody analysis for audio. These auxiliary tasks help the model identify emotion-relevant cues in each modality before fusion, reducing reliance on spurious correlations in low-resource settings. Experiments on IndoMER show that OmniMER achieves 0.582 Macro-F1 on sentiment classification and 0.454 on emotion recognition, outperforming the base model by 7.6 and 22.1 absolute points respectively. Cross-lingual evaluation on the Chinese CH-SIMS dataset further demonstrates the generalizability of the proposed framework. The dataset and code are publicly available. https://github.com/yanxm01/INDOMER


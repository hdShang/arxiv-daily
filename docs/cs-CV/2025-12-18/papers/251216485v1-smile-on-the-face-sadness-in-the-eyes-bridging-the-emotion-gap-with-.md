---
layout: default
title: Smile on the Face, Sadness in the Eyes: Bridging the Emotion Gap with a Multimodal Dataset of Eye and Facial Behaviors
---

# Smile on the Face, Sadness in the Eyes: Bridging the Emotion Gap with a Multimodal Dataset of Eye and Facial Behaviors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16485" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16485v1</a>
  <a href="https://arxiv.org/pdf/2512.16485.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16485v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16485v1', 'Smile on the Face, Sadness in the Eyes: Bridging the Emotion Gap with a Multimodal Dataset of Eye and Facial Behaviors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kejun Liu, Yuanyuan Liu, Lin Wei, Chang Tang, Yibing Zhan, Zijing Chen, Zhe Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

**备注**: Accepted by TMM

**🔗 代码/项目**: [GITHUB](https://github.com/kejun1/EMER)

---

## 💡 一句话要点

**提出EMER数据集和EMERT模型，利用眼部行为弥合面部表情识别和情感识别之间的差距**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感识别` `多模态融合` `眼部行为` `面部表情` `Transformer` `对抗学习` `数据集`

## 📋 核心要点

1. 现有情感识别主要依赖面部表情，但面部表情常作为社交工具，无法真实反映内心情感。
2. 论文提出将眼部行为作为情感线索，构建EMER数据集，并设计EMERT模型弥合情感差距。
3. 实验结果表明，EMERT模型在EMER数据集上显著优于其他多模态方法，验证了眼部行为的重要性。

## 📝 摘要（中文）

情感识别(ER)是从感知数据中分析和识别人类情感的过程。目前，该领域严重依赖于面部表情识别(FER)，因为视觉通道传递丰富的情感线索。然而，面部表情通常被用作社交工具，而不是真实内心情感的体现。为了理解和弥合FER和ER之间的差距，我们引入眼部行为作为一个重要的情感线索，并构建了一个眼部行为辅助的多模态情感识别(EMER)数据集。为了收集具有真实情感的数据，我们利用刺激材料进行自发情感诱导，在此过程中，非侵入性的眼部行为数据，如眼动序列和眼部注视图，与面部表情视频一起被捕获。为了更好地说明ER和FER之间的差距，我们分别对多模态ER和FER进行多视角情感标注。此外，基于新的数据集，我们设计了一个简单而有效的眼部行为辅助的MER Transformer (EMERT)，通过弥合情感差距来增强ER。EMERT利用模态对抗特征解耦和一个多任务Transformer来建模眼部行为，作为面部表情的有力补充。在实验中，我们为EMER数据集引入了七个多模态基准协议，用于各种综合评估。结果表明，EMERT优于其他最先进的多模态方法，揭示了建模眼部行为对于鲁棒ER的重要性。总而言之，我们对眼部行为在ER中的重要性进行了全面的分析，从而推进了解决FER和ER之间差距的研究，以获得更强大的ER性能。我们的EMER数据集和训练好的EMERT模型将在https://github.com/kejun1/EMER上公开。

## 🔬 方法详解

**问题定义**：现有情感识别方法过度依赖面部表情，忽略了面部表情可能存在的伪装性，导致情感识别的准确性受到影响。因此，需要一种更鲁棒的情感识别方法，能够克服面部表情的局限性，更准确地捕捉真实的情感状态。

**核心思路**：论文的核心思路是将眼部行为作为情感识别的重要补充信息。眼部行为，如眼动序列和眼部注视图，能够反映个体的情绪状态，并且相对于面部表情更难伪装。通过融合眼部行为和面部表情信息，可以提高情感识别的准确性和鲁棒性。

**技术框架**：论文提出的EMERT模型主要包含以下几个模块：1)模态对抗特征解耦模块，用于分离面部表情和眼部行为中的情感相关和情感无关特征；2)多任务Transformer模块，用于融合解耦后的面部表情和眼部行为特征，并同时预测情感标签和眼部行为标签。整体流程是：输入面部表情视频和眼部行为数据，经过特征提取和解耦后，输入到多任务Transformer中进行情感预测。

**关键创新**：论文的关键创新在于：1)提出了将眼部行为作为情感识别的重要线索，并构建了相应的多模态数据集EMER；2)设计了模态对抗特征解耦模块，能够有效分离不同模态中的情感相关和情感无关特征；3)提出了多任务Transformer模型，能够同时学习情感和眼部行为的表示。与现有方法相比，EMERT模型能够更有效地利用眼部行为信息，提高情感识别的准确性和鲁棒性。

**关键设计**：在模态对抗特征解耦模块中，使用了梯度反转层(Gradient Reversal Layer)来实现对抗训练，从而分离情感相关和情感无关特征。在多任务Transformer模块中，使用了交叉注意力机制(Cross-Attention)来融合不同模态的特征。损失函数包括情感分类损失和眼部行为预测损失，通过联合优化这两个损失函数来提高模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16485v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16485v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16485v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EMERT模型在EMER数据集上取得了显著的性能提升，优于其他最先进的多模态情感识别方法。具体而言，EMERT模型在七个多模态基准协议上都取得了最佳性能，证明了眼部行为在情感识别中的重要性，以及EMERT模型有效融合多模态信息的能力。

## 🎯 应用场景

该研究成果可应用于人机交互、心理健康评估、智能客服等领域。通过结合面部表情和眼部行为进行情感识别，可以提高人机交互的自然性和准确性，帮助心理医生更准确地评估患者的情绪状态，并使智能客服能够更好地理解用户的情感需求。

## 📄 摘要（原文）

> Emotion Recognition (ER) is the process of analyzing and identifying human emotions from sensing data. Currently, the field heavily relies on facial expression recognition (FER) because visual channel conveys rich emotional cues. However, facial expressions are often used as social tools rather than manifestations of genuine inner emotions. To understand and bridge this gap between FER and ER, we introduce eye behaviors as an important emotional cue and construct an Eye-behavior-aided Multimodal Emotion Recognition (EMER) dataset. To collect data with genuine emotions, spontaneous emotion induction paradigm is exploited with stimulus material, during which non-invasive eye behavior data, like eye movement sequences and eye fixation maps, is captured together with facial expression videos. To better illustrate the gap between ER and FER, multi-view emotion labels for mutimodal ER and FER are separately annotated. Furthermore, based on the new dataset, we design a simple yet effective Eye-behavior-aided MER Transformer (EMERT) that enhances ER by bridging the emotion gap. EMERT leverages modality-adversarial feature decoupling and a multitask Transformer to model eye behaviors as a strong complement to facial expressions. In the experiment, we introduce seven multimodal benchmark protocols for a variety of comprehensive evaluations of the EMER dataset. The results show that the EMERT outperforms other state-of-the-art multimodal methods by a great margin, revealing the importance of modeling eye behaviors for robust ER. To sum up, we provide a comprehensive analysis of the importance of eye behaviors in ER, advancing the study on addressing the gap between FER and ER for more robust ER performance. Our EMER dataset and the trained EMERT models will be publicly available at https://github.com/kejun1/EMER.


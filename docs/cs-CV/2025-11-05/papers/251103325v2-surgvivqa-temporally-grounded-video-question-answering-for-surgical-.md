---
layout: default
title: SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding
---

# SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03325" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03325v2</a>
  <a href="https://arxiv.org/pdf/2511.03325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03325v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03325v2', 'SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mauro Orazio Drago, Luca Carlini, Pelinsu Celebi Balyemez, Dennis Pierantozzi, Chiara Lena, Cesare Hassan, Danail Stoyanov, Elena De Momi, Sophia Bano, Mobarak I. Hoque

**分类**: cs.CV

**发布日期**: 2025-11-05 (更新: 2025-11-06)

**🔗 代码/项目**: [GITHUB](https://github.com/madratak/SurgViVQA)

---

## 💡 一句话要点

**SurgViVQA：面向手术场景理解的时序视频问答模型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `手术视频问答` `时序建模` `视频理解` `多模态融合` `Transformer` `医学影像` `内窥镜视频`

## 📋 核心要点

1. 现有手术视频问答方法依赖静态图像特征，忽略了手术过程中的时序动态信息，限制了模型对手术过程的理解。
2. SurgViVQA通过Masked Video-Text Encoder融合视频和问题特征，捕捉运动和工具-组织交互等时序信息，提升模型对动态手术场景的理解能力。
3. 在REAL-Colon-VQA和EndoVis18-VQA数据集上的实验表明，SurgViVQA在关键词准确率上优于现有模型，分别提升了11%和9%。

## 📝 摘要（中文）

手术领域的视频问答(VideoQA)旨在通过使AI模型能够推理时间上连贯的事件，而不是孤立的帧，来增强术中理解。目前的方法仅限于静态图像特征，并且可用的数据集通常缺乏时间注释，忽略了对于准确程序解释至关重要的动态信息。我们提出了SurgViVQA，一种手术VideoQA模型，它将视觉推理从静态图像扩展到动态手术场景。它使用Masked Video-Text Encoder来融合视频和问题特征，捕捉运动和工具-组织交互等时间线索，然后由微调的大型语言模型(LLM)将其解码为连贯的答案。为了评估其性能，我们整理了REAL-Colon-VQA，一个结肠镜视频数据集，包括与运动相关的问题和诊断属性，以及具有改写或语义改变的公式的模板外问题，以评估模型的鲁棒性。在REAL-Colon-VQA和公共EndoVis18-VQA数据集上的实验验证表明，SurgViVQA优于现有的基于图像的VQA基准模型，尤其是在关键词准确率方面，在REAL-Colon-VQA上比PitVQA提高了+11%，在EndoVis18-VQA上提高了+9%。对问题的扰动研究进一步证实了改进的泛化性和对问题措辞变化的鲁棒性。SurgViVQA和REAL-Colon-VQA数据集为手术VideoQA中具有时间意识的理解提供了一个框架，使AI模型能够更有效地解释动态程序上下文。

## 🔬 方法详解

**问题定义**：现有手术视频问答方法主要基于静态图像，无法有效利用手术过程中的时序信息，例如工具运动、组织形变等。这导致模型难以准确理解手术步骤和关键事件，限制了其在术中辅助决策中的应用。现有数据集也缺乏足够的时间标注，进一步加剧了这个问题。

**核心思路**：SurgViVQA的核心思路是将视频和问题进行联合编码，利用Transformer架构捕捉视频中的时序依赖关系，并将其与问题语义进行对齐。通过这种方式，模型可以更好地理解手术过程中的动态变化，并根据问题给出准确的答案。

**技术框架**：SurgViVQA主要包含以下几个模块：1) 视频特征提取模块：使用预训练的视觉模型（例如ResNet或TimeSformer）提取视频帧的视觉特征。2) 问题特征提取模块：使用预训练的文本模型（例如BERT）提取问题的文本特征。3) Masked Video-Text Encoder：使用Transformer架构，将视频特征和问题特征进行融合，学习视频和问题之间的时序依赖关系。该模块采用Masked Language Modeling (MLM) 预训练方式，提升模型对上下文信息的理解能力。4) 解码器：使用微调的大型语言模型（LLM）将融合后的特征解码为答案。

**关键创新**：SurgViVQA的关键创新在于其Masked Video-Text Encoder，它能够有效地捕捉视频中的时序信息，并将其与问题语义进行对齐。与现有方法相比，SurgViVQA能够更好地理解手术过程中的动态变化，从而给出更准确的答案。此外，REAL-Colon-VQA数据集的构建也为该领域的研究提供了新的资源。

**关键设计**：Masked Video-Text Encoder采用多层Transformer结构，每一层包含自注意力机制和前馈神经网络。自注意力机制用于捕捉视频帧之间的时序依赖关系，前馈神经网络用于学习特征的非线性变换。在训练过程中，采用Masked Language Modeling (MLM) 预训练方式，随机mask掉一部分视频帧或问题中的词语，然后让模型预测被mask掉的内容。这种预训练方式可以提升模型对上下文信息的理解能力。解码器部分，选择合适的LLM并进行微调，以适应手术视频问答任务的特点。

## 📊 实验亮点

SurgViVQA在REAL-Colon-VQA和EndoVis18-VQA数据集上取得了显著的性能提升。在REAL-Colon-VQA数据集上，SurgViVQA的关键词准确率比PitVQA提高了11%。在EndoVis18-VQA数据集上，SurgViVQA的关键词准确率比PitVQA提高了9%。此外，对问题的扰动研究表明，SurgViVQA具有更好的泛化性和对问题措辞变化的鲁棒性。

## 🎯 应用场景

SurgViVQA具有广泛的应用前景，可用于术中导航、手术技能评估、手术机器人控制等领域。通过理解手术视频中的时序信息，SurgViVQA可以为医生提供实时的手术指导，帮助他们更好地完成手术。此外，SurgViVQA还可以用于评估医生的手术技能，为手术机器人的控制提供更准确的指令。未来，SurgViVQA有望成为智能手术室的重要组成部分。

## 📄 摘要（原文）

> Video Question Answering (VideoQA) in the surgical domain aims to enhance intraoperative understanding by enabling AI models to reason over temporally coherent events rather than isolated frames. Current approaches are limited to static image features, and available datasets often lack temporal annotations, ignoring the dynamics critical for accurate procedural interpretation. We propose SurgViVQA, a surgical VideoQA model that extends visual reasoning from static images to dynamic surgical scenes. It uses a Masked Video--Text Encoder to fuse video and question features, capturing temporal cues such as motion and tool--tissue interactions, which a fine-tuned large language model (LLM) then decodes into coherent answers. To evaluate its performance, we curated REAL-Colon-VQA, a colonoscopic video dataset that includes motion-related questions and diagnostic attributes, as well as out-of-template questions with rephrased or semantically altered formulations to assess model robustness. Experimental validation on REAL-Colon-VQA and the public EndoVis18-VQA dataset shows that SurgViVQA outperforms existing image-based VQA benchmark models, particularly in keyword accuracy, improving over PitVQA by +11\% on REAL-Colon-VQA and +9\% on EndoVis18-VQA. A perturbation study on the questions further confirms improved generalizability and robustness to variations in question phrasing. SurgViVQA and the REAL-Colon-VQA dataset provide a framework for temporally-aware understanding in surgical VideoQA, enabling AI models to interpret dynamic procedural contexts more effectively. Code and dataset available at https://github.com/madratak/SurgViVQA.


---
layout: default
title: "Cognitive Linguistic Identity Fusion Score (CLIFS): A Scalable Cognition-Informed Approach to Quantifying Identity Fusion from Text"
---

# Cognitive Linguistic Identity Fusion Score (CLIFS): A Scalable Cognition-Informed Approach to Quantifying Identity Fusion from Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16813" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16813v1</a>
  <a href="https://arxiv.org/pdf/2509.16813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16813v1', 'Cognitive Linguistic Identity Fusion Score (CLIFS): A Scalable Cognition-Informed Approach to Quantifying Identity Fusion from Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Devin R. Wright, Jisun An, Yong-Yeol Ahn

**分类**: cs.CL

**发布日期**: 2025-09-20

**备注**: Authors' accepted manuscript (postprint; camera-ready). To appear in the Proceedings of EMNLP 2025. Pagination/footer layout may differ from the Version of Record

**🔗 代码/项目**: [GITHUB](https://github.com/DevinW-sudo/CLIFS)

---

## 💡 一句话要点

**提出CLIFS，一种基于认知语言学和LLM的可扩展身份融合量化方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `身份融合` `认知语言学` `大型语言模型` `隐喻检测` `暴力风险评估`

## 📋 核心要点

1. 现有身份融合量化方法依赖于人工调查，成本高昂且难以大规模应用。
2. CLIFS利用认知语言学和大型语言模型，通过隐喻检测自动评估文本中的身份融合程度。
3. 实验表明，CLIFS在基准测试中优于现有自动化方法和人工标注，并在暴力风险评估中提升显著。

## 📝 摘要（中文）

本文提出了一种新的指标——认知语言学身份融合评分（CLIFS），它将认知语言学与大型语言模型（LLM）相结合，构建于隐喻检测之上，用于量化身份融合，即个体将自我与另一实体或抽象目标（如宗教团体、政党、意识形态等）在心理上融合的程度。与需要控制调查或直接实地接触的传统图像和语言量表不同，CLIFS提供完全自动化、可扩展的评估，同时与已建立的语言测量方法保持高度一致。在基准测试中，CLIFS优于现有的自动化方法和人工标注。作为概念验证，我们将CLIFS应用于暴力风险评估，证明它可以将暴力风险评估的准确率提高240%以上。基于我们对新NLP任务的识别和早期成功，我们强调需要开发更大、更多样化的数据集，涵盖额外的融合目标领域和文化背景，以增强泛化性并进一步推进这一新兴领域。CLIFS模型和代码已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决身份融合的量化问题，即如何从文本中自动且准确地评估个体与特定目标（如群体、信仰等）的融合程度。现有方法，如问卷调查等，需要人工参与，成本高，难以大规模应用，且可能存在主观偏差。

**核心思路**：论文的核心思路是利用认知语言学理论，认为身份融合可以通过语言中的隐喻来体现。例如，当一个人高度认同某个群体时，他/她可能会使用与该群体相关的隐喻来描述自己。通过检测文本中与特定目标相关的隐喻，可以推断出个体与该目标的融合程度。

**技术框架**：CLIFS的技术框架主要包括以下几个阶段：1) **文本预处理**：对输入的文本进行清洗和标准化。2) **隐喻检测**：利用大型语言模型（LLM）检测文本中与目标相关的隐喻。具体来说，论文可能使用了预训练的语言模型，并针对隐喻检测任务进行了微调。3) **融合评分计算**：根据检测到的隐喻数量和强度，计算身份融合评分。评分越高，表示融合程度越高。4) **模型评估**：将CLIFS的评分与人工标注或其他自动化方法的评分进行比较，评估其准确性和可靠性。

**关键创新**：CLIFS的关键创新在于将认知语言学理论与大型语言模型相结合，提出了一种全新的身份融合量化方法。与传统的基于问卷调查的方法相比，CLIFS具有自动化、可扩展和低成本的优势。与现有的自动化方法相比，CLIFS更注重语言中的隐喻，能够更准确地捕捉个体与目标之间的心理联系。

**关键设计**：论文可能使用了特定的提示工程（prompt engineering）技术来指导LLM进行隐喻检测。例如，可以设计特定的提示语，要求LLM识别文本中与目标相关的隐喻，并给出相应的解释。此外，论文可能还使用了特定的损失函数来训练LLM，以提高其隐喻检测的准确性。具体的参数设置和网络结构等技术细节需要在论文原文中查找。

## 📊 实验亮点

CLIFS在基准测试中优于现有的自动化方法和人工标注，表明其具有较高的准确性和可靠性。在暴力风险评估的应用中，CLIFS将评估准确率提高了240%以上，证明了其在实际应用中的巨大潜力。这些结果表明，CLIFS是一种有价值的身份融合量化工具。

## 🎯 应用场景

CLIFS具有广泛的应用前景，例如：1) 暴力风险评估：通过分析社交媒体文本，预测个体参与暴力行为的风险。2) 政治倾向分析：通过分析政治言论，了解个体对不同政治立场的认同程度。3) 品牌忠诚度分析：通过分析消费者评论，评估消费者对特定品牌的忠诚度。该研究有助于更深入地理解群体行为，并为相关决策提供支持。

## 📄 摘要（原文）

> Quantifying identity fusion -- the psychological merging of self with another entity or abstract target (e.g., a religious group, political party, ideology, value, brand, belief, etc.) -- is vital for understanding a wide range of group-based human behaviors. We introduce the Cognitive Linguistic Identity Fusion Score (CLIFS), a novel metric that integrates cognitive linguistics with large language models (LLMs), which builds on implicit metaphor detection. Unlike traditional pictorial and verbal scales, which require controlled surveys or direct field contact, CLIFS delivers fully automated, scalable assessments while maintaining strong alignment with the established verbal measure. In benchmarks, CLIFS outperforms both existing automated approaches and human annotation. As a proof of concept, we apply CLIFS to violence risk assessment to demonstrate that it can improve violence risk assessment by more than 240%. Building on our identification of a new NLP task and early success, we underscore the need to develop larger, more diverse datasets that encompass additional fusion-target domains and cultural backgrounds to enhance generalizability and further advance this emerging area. CLIFS models and code are public at https://github.com/DevinW-sudo/CLIFS.


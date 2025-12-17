---
layout: default
title: CML-Bench: A Framework for Evaluating and Enhancing LLM-Powered Movie Scripts Generation
---

# CML-Bench: A Framework for Evaluating and Enhancing LLM-Powered Movie Scripts Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06231" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06231v1</a>
  <a href="https://arxiv.org/pdf/2510.06231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06231v1" onclick="toggleFavorite(this, '2510.06231v1', 'CML-Bench: A Framework for Evaluating and Enhancing LLM-Powered Movie Scripts Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingzhe Zheng, Dingjie Song, Guanyu Zhou, Jun You, Jiahao Zhan, Xuran Ma, Xinyuan Song, Ser-Nam Lim, Qifeng Chen, Harry Yang

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-01

**备注**: 24 pages, 9 figures

---

## 💡 一句话要点

**CML-Bench：用于评估和提升大语言模型生成电影剧本的框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电影剧本生成` `大语言模型` `质量评估` `叙事连贯性` `角色一致性`

## 📋 核心要点

1. 现有大语言模型在生成电影剧本时，难以捕捉到剧本中细致的叙事和情感深度，缺乏“灵魂”。
2. 论文提出CML-Bench框架，通过对话连贯性、角色一致性和情节合理性三个维度来评估剧本质量。
3. 实验表明，CML-Bench能有效评估剧本质量，并结合CML-Instruction提示策略能提升LLM生成剧本的质量。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成高度结构化文本方面表现出了卓越的能力。然而，电影剧本在结构组织良好的同时，还需要细致入微的叙事和情感深度——这是引人入胜的电影的“灵魂”，而LLMs往往无法捕捉到这一点。为了研究这种不足，我们首先整理了CML-Dataset，这是一个包含电影标记语言（CML）的（摘要，内容）对的数据集，其中“内容”由高质量电影剧本的片段组成，“摘要”是对内容的简明描述。通过深入分析这些真实剧本中内在的多镜头连续性和叙事结构，我们确定了质量评估的三个关键维度：对话连贯性（DC）、角色一致性（CC）和情节合理性（PR）。基于这些发现，我们提出了CML-Bench，其中包含跨这些维度的定量指标。CML-Bench有效地为精心编写的人工剧本分配高分，同时准确地指出LLMs生成的剧本中的弱点。为了进一步验证我们的基准，我们引入了CML-Instruction，这是一种提示策略，包含关于角色对话和事件逻辑的详细说明，以指导LLMs生成更结构化和更具电影感的剧本。大量的实验验证了我们基准的有效性，并表明在CML-Instruction指导下的LLMs生成了更高质量的剧本，其结果与人类偏好相符。

## 🔬 方法详解

**问题定义**：现有的大语言模型在生成电影剧本时，虽然能够生成结构化的文本，但难以捕捉到电影剧本中细致的叙事和情感深度，导致生成的剧本缺乏“灵魂”。现有方法缺乏对剧本质量的有效评估和提升手段。

**核心思路**：论文的核心思路是通过构建一个包含高质量电影剧本的数据集CML-Dataset，并基于对剧本内在结构和叙事特点的分析，提出三个关键的质量评估维度：对话连贯性、角色一致性和情节合理性。然后，基于这些维度构建CML-Bench基准，用于评估LLM生成的剧本质量。此外，还提出了CML-Instruction提示策略，通过详细的指令来指导LLM生成更高质量的剧本。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 构建CML-Dataset数据集，包含电影剧本片段和对应的摘要；2) 分析剧本的内在结构和叙事特点，确定对话连贯性、角色一致性和情节合理性三个质量评估维度；3) 构建CML-Bench基准，包含跨这些维度的定量指标；4) 提出CML-Instruction提示策略，用于指导LLM生成剧本；5) 进行实验，验证CML-Bench的有效性和CML-Instruction的提升效果。

**关键创新**：该论文的关键创新在于：1) 提出了CML-Bench基准，能够有效地评估LLM生成的电影剧本的质量，并能准确地指出剧本中的弱点；2) 提出了CML-Instruction提示策略，能够有效地指导LLM生成更高质量的剧本，其结果与人类偏好相符。与现有方法相比，该论文更关注剧本的叙事和情感深度，并提出了相应的评估和提升方法。

**关键设计**：CML-Bench的关键设计在于对话连贯性（DC）、角色一致性（CC）和情节合理性（PR）三个维度的定量指标的设计。CML-Instruction的关键设计在于详细的指令，包括角色对话和事件逻辑，这些指令能够有效地指导LLM生成更结构化和更具电影感的剧本。具体的参数设置、损失函数、网络结构等技术细节在论文中没有详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，CML-Bench能够有效区分人工撰写的高质量剧本和LLM生成的剧本，并能准确指出LLM生成剧本的不足之处。在CML-Instruction的指导下，LLM生成的剧本质量显著提升，与人类偏好更加一致。具体的性能数据和提升幅度在论文中没有明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于电影剧本自动生成、剧本质量评估、编剧辅助工具等领域。通过CML-Bench，可以客观评估LLM生成的剧本质量，并指导LLM生成更符合人类偏好的剧本。未来，该研究可以进一步扩展到其他类型的创意文本生成领域，例如小说、游戏剧本等，具有广阔的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable proficiency in generating highly structured texts. However, while exhibiting a high degree of structural organization, movie scripts demand an additional layer of nuanced storytelling and emotional depth-the 'soul' of compelling cinema-that LLMs often fail to capture. To investigate this deficiency, we first curated CML-Dataset, a dataset comprising (summary, content) pairs for Cinematic Markup Language (CML), where 'content' consists of segments from esteemed, high-quality movie scripts and 'summary' is a concise description of the content. Through an in-depth analysis of the intrinsic multi-shot continuity and narrative structures within these authentic scripts, we identified three pivotal dimensions for quality assessment: Dialogue Coherence (DC), Character Consistency (CC), and Plot Reasonableness (PR). Informed by these findings, we propose the CML-Bench, featuring quantitative metrics across these dimensions. CML-Bench effectively assigns high scores to well-crafted, human-written scripts while concurrently pinpointing the weaknesses in screenplays generated by LLMs. To further validate our benchmark, we introduce CML-Instruction, a prompting strategy with detailed instructions on character dialogue and event logic, to guide LLMs to generate more structured and cinematically sound scripts. Extensive experiments validate the effectiveness of our benchmark and demonstrate that LLMs guided by CML-Instruction generate higher-quality screenplays, with results aligned with human preferences.


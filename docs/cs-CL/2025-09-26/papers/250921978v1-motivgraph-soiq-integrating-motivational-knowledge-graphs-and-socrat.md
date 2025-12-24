---
layout: default
title: "MotivGraph-SoIQ: Integrating Motivational Knowledge Graphs and Socratic Dialogue for Enhanced LLM Ideation"
---

# MotivGraph-SoIQ: Integrating Motivational Knowledge Graphs and Socratic Dialogue for Enhanced LLM Ideation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21978" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21978v1</a>
  <a href="https://arxiv.org/pdf/2509.21978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21978v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21978v1', 'MotivGraph-SoIQ: Integrating Motivational Knowledge Graphs and Socratic Dialogue for Enhanced LLM Ideation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinping Lei, Tong Zhou, Yubo Chen, Kang Liu, Jun Zhao

**分类**: cs.CL

**发布日期**: 2025-09-26

**备注**: EMNLP2025 Findings

---

## 💡 一句话要点

**MotivGraph-SoIQ：融合动机知识图谱与苏格拉底式对话，增强LLM学术创意生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识图谱` `苏格拉底式对话` `创意生成` `学术创新`

## 📋 核心要点

1. 现有LLM在学术创意生成中存在缺乏依据和确认偏差的问题，限制了其进一步发展。
2. MotivGraph-SoIQ融合动机知识图谱和苏格拉底式对话，为LLM提供依据并改进创意。
3. 实验表明，MotivGraph-SoIQ在多个指标上优于现有方法，提升了创意质量。

## 📝 摘要（中文）

大型语言模型（LLM）在加速学术创意生成方面具有巨大潜力，但面临着创意缺乏依据和确认偏差等关键挑战，阻碍了进一步的完善。我们提出了一种融合动机知识图谱和苏格拉底式对话的新框架，称为MotivGraph-SoIQ，以增强LLM的创意生成能力。该框架通过整合动机知识图谱（MotivGraph）和一个Q驱动的苏格拉底式创意器，为LLM的创意生成过程提供必要的依据和实际的创意改进步骤。MotivGraph以结构化的方式存储三种关键节点类型（问题、挑战和解决方案），为LLM的创意过程提供动机基础。创意器是一个双代理系统，利用苏格拉底式提问，促进严格的完善过程，从而减轻确认偏差，并在新颖性、实验严谨性和动机合理性维度上提高创意质量。在ICLR25论文主题数据集上，MotivGraph-SoIQ在基于LLM的评分、ELO排名和人工评估指标方面均表现出优于现有最先进方法的优势。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在学术创意生成方面面临两个主要问题：一是生成的创意缺乏充分的依据，容易产生空想；二是容易受到确认偏差的影响，难以进行有效的改进和完善。这些问题限制了LLM在学术研究中的应用潜力。

**核心思路**：MotivGraph-SoIQ的核心思路是利用动机知识图谱（MotivGraph）为LLM提供创意生成的依据，并通过苏格拉底式对话引导LLM进行深入思考和批判性评估，从而减轻确认偏差，提高创意质量。这种方法结合了知识图谱的结构化知识和苏格拉底式对话的启发式引导，旨在弥补LLM在创意生成方面的不足。

**技术框架**：MotivGraph-SoIQ框架包含两个主要组成部分：动机知识图谱（MotivGraph）和Q驱动的苏格拉底式创意器。MotivGraph以结构化的方式存储问题、挑战和解决方案三种关键节点，为LLM提供动机基础。苏格拉底式创意器是一个双代理系统，通过提问和回答的方式，引导LLM进行创意完善，减轻确认偏差。整个流程包括：1) LLM基于MotivGraph生成初始创意；2) 苏格拉底式创意器对创意进行提问和评估；3) LLM根据提问和评估结果改进创意；4) 重复步骤2和3，直到创意达到满意的质量。

**关键创新**：MotivGraph-SoIQ的关键创新在于将动机知识图谱和苏格拉底式对话相结合，为LLM的创意生成过程提供了一种结构化和启发式的引导方法。与传统的LLM创意生成方法相比，MotivGraph-SoIQ能够更好地利用知识，减轻确认偏差，并提高创意质量。此外，双代理苏格拉底式对话的设计也为创意完善提供了一种新颖的思路。

**关键设计**：MotivGraph的设计包括定义问题、挑战和解决方案三种节点类型，并建立它们之间的关系。苏格拉底式创意器的设计包括定义提问和回答的策略，以及评估创意质量的指标（如新颖性、实验严谨性和动机合理性）。具体参数设置和损失函数等技术细节在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

MotivGraph-SoIQ在ICLR25论文主题数据集上取得了显著的实验结果。通过LLM评分、ELO排名和人工评估等多种指标，MotivGraph-SoIQ均优于现有的最先进方法。这些结果表明，MotivGraph-SoIQ能够有效地提高LLM创意生成的新颖性、实验严谨性和动机合理性。

## 🎯 应用场景

MotivGraph-SoIQ可应用于学术研究、创新设计、问题解决等领域。它能够帮助研究人员和设计师更有效地利用LLM进行创意生成，并提高创意质量。该研究的潜在价值在于加速学术创新，促进跨学科合作，并为解决复杂问题提供新的思路。未来，该方法有望扩展到其他领域，如商业策划、政策制定等。

## 📄 摘要（原文）

> Large Language Models (LLMs) hold substantial potential for accelerating academic ideation but face critical challenges in grounding ideas and mitigating confirmation bias for further refinement. We propose integrating motivational knowledge graphs and socratic dialogue to address these limitations in enhanced LLM ideation (MotivGraph-SoIQ). This novel framework provides essential grounding and practical idea improvement steps for LLM ideation by integrating a Motivational Knowledge Graph (MotivGraph) with a Q-Driven Socratic Ideator. The MotivGraph structurally stores three key node types(problem, challenge and solution) to offer motivation grounding for the LLM ideation process. The Ideator is a dual-agent system utilizing Socratic questioning, which facilitates a rigorous refinement process that mitigates confirmation bias and improves idea quality across novelty, experimental rigor, and motivational rationality dimensions. On the ICLR25 paper topics dataset, MotivGraph-SoIQ exhibits clear advantages over existing state-of-the-art approaches across LLM-based scoring, ELO ranking, and human evaluation metrics.


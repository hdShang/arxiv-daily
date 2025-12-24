---
layout: default
title: "LLM-as-a-Fuzzy-Judge: Fine-Tuning Large Language Models as a Clinical Evaluation Judge with Fuzzy Logic"
---

# LLM-as-a-Fuzzy-Judge: Fine-Tuning Large Language Models as a Clinical Evaluation Judge with Fuzzy Logic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11221" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11221v1</a>
  <a href="https://arxiv.org/pdf/2506.11221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11221v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11221v1', 'LLM-as-a-Fuzzy-Judge: Fine-Tuning Large Language Models as a Clinical Evaluation Judge with Fuzzy Logic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weibing Zheng, Laurah Turner, Jess Kropczynski, Murat Ozer, Tri Nguyen, Shane Halse

**分类**: cs.AI, cs.CL, cs.LO

**发布日期**: 2025-06-12

**备注**: 12 pages, 1 figure, 2025 IFSA World Congress NAFIPS Annual Meeting

**🔗 代码/项目**: [GITHUB](https://github.com/2sigmaEdTech/LLMAsAJudge)

---

## 💡 一句话要点

**提出LLM-as-a-Fuzzy-Judge以解决临床评估自动化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `模糊逻辑` `临床评估` `医学教育` `自动化评估` `监督微调` `人类偏好对齐`

## 📋 核心要点

1. 现有方法在自动化评估医学学生的临床沟通技能时，难以与医生的主观判断保持一致。
2. 论文提出LLM-as-a-Fuzzy-Judge，通过模糊逻辑对LLM进行微调，以评估医学学生在与AI患者对话中的表现。
3. 实验结果表明，该方法在评估准确率上超过80%，并在主要标准项上超过90%，有效提升了评估的可解释性和人类对齐性。

## 📝 摘要（中文）

临床沟通技能在医学教育中至关重要，但大规模评估这些技能面临挑战。尽管基于大型语言模型（LLM）的临床场景模拟在提升医学学生的临床实践方面显示出潜力，但自动化评估与医生主观判断之间的对齐仍然困难。本文提出LLM-as-a-Fuzzy-Judge，通过结合模糊逻辑和LLM，旨在解决医学学生临床技能的自动评估与医生偏好之间的对齐问题。该方法通过对医学教育系统的数据收集、基于多维模糊集的数据标注、提示工程和对预训练LLM的监督微调，最终实现了超过80%的准确率，主要标准项超过90%。

## 🔬 方法详解

**问题定义**：本文旨在解决医学教育中临床沟通技能的自动化评估问题，现有方法难以捕捉医生的主观判断和细微差别。

**核心思路**：通过结合模糊逻辑与大型语言模型（LLM），对LLM进行微调，使其能够基于人类标注的模糊集评估医学学生的表现，从而实现更符合人类偏好的自动评估。

**技术框架**：整体流程包括数据收集、数据标注、提示工程和对预训练LLM的监督微调。数据收集来自LLM驱动的医学教育系统，标注基于四个模糊集：专业性、医学相关性、伦理行为和情境干扰。

**关键创新**：最重要的创新在于将模糊逻辑与LLM结合，形成LLM-as-a-Fuzzy-Judge，能够更好地对齐人类评估标准，提升评估的可解释性。

**关键设计**：在微调过程中，采用了基于人类标注的多维模糊集作为训练数据，设计了相应的损失函数以优化模型的评估能力。

## 📊 实验亮点

实验结果显示，LLM-as-a-Fuzzy-Judge在评估准确率上超过80%，其中主要标准项的准确率超过90%。这一成果表明，结合模糊逻辑与LLM的评估方法在医学教育中具有显著的提升效果，能够有效支持更为人性化的评估实践。

## 🎯 应用场景

该研究的潜在应用领域包括医学教育、临床培训和自动化评估系统。通过提供更符合人类判断的评估工具，能够帮助医学教育机构提升教学质量，促进学生的临床沟通能力发展，未来可能对医学教育的评估标准产生深远影响。

## 📄 摘要（原文）

> Clinical communication skills are critical in medical education, and practicing and assessing clinical communication skills on a scale is challenging. Although LLM-powered clinical scenario simulations have shown promise in enhancing medical students' clinical practice, providing automated and scalable clinical evaluation that follows nuanced physician judgment is difficult. This paper combines fuzzy logic and Large Language Model (LLM) and proposes LLM-as-a-Fuzzy-Judge to address the challenge of aligning the automated evaluation of medical students' clinical skills with subjective physicians' preferences. LLM-as-a-Fuzzy-Judge is an approach that LLM is fine-tuned to evaluate medical students' utterances within student-AI patient conversation scripts based on human annotations from four fuzzy sets, including Professionalism, Medical Relevance, Ethical Behavior, and Contextual Distraction. The methodology of this paper started from data collection from the LLM-powered medical education system, data annotation based on multidimensional fuzzy sets, followed by prompt engineering and the supervised fine-tuning (SFT) of the pre-trained LLMs using these human annotations. The results show that the LLM-as-a-Fuzzy-Judge achieves over 80\% accuracy, with major criteria items over 90\%, effectively leveraging fuzzy logic and LLM as a solution to deliver interpretable, human-aligned assessment. This work suggests the viability of leveraging fuzzy logic and LLM to align with human preferences, advances automated evaluation in medical education, and supports more robust assessment and judgment practices. The GitHub repository of this work is available at https://github.com/2sigmaEdTech/LLMAsAJudge


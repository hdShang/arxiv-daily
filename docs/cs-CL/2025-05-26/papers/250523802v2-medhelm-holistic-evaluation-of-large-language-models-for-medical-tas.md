---
layout: default
title: MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks
---

# MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23802" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23802v2</a>
  <a href="https://arxiv.org/pdf/2505.23802.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23802v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23802v2', 'MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suhana Bedi, Hejie Cui, Miguel Fuentes, Alyssa Unell, Michael Wornow, Juan M. Banda, Nikesh Kotecha, Timothy Keyes, Yifan Mai, Mert Oez, Hao Qiu, Shrey Jain, Leonardo Schettini, Mehr Kashyap, Jason Alan Fries, Akshay Swaminathan, Philip Chung, Fateme Nateghi, Asad Aali, Ashwin Nayak, Shivam Vedak, Sneha S. Jain, Birju Patel, Oluseyi Fayanju, Shreya Shah, Ethan Goh, Dong-han Yao, Brian Soetikno, Eduardo Reis, Sergios Gatidis, Vasu Divi, Robson Capasso, Rachna Saralkar, Chia-Chun Chiang, Jenelle Jindal, Tho Pham, Faraz Ghoddusi, Steven Lin, Albert S. Chiou, Christy Hong, Mohana Roy, Michael F. Gensheimer, Hinesh Patel, Kevin Schulman, Dev Dash, Danton Char, Lance Downing, Francois Grolleau, Kameron Black, Bethel Mieso, Aydin Zahedivash, Wen-wai Yim, Harshita Sharma, Tony Lee, Hannah Kirsch, Jennifer Lee, Nerissa Ambers, Carlene Lugtu, Aditya Sharma, Bilal Mawji, Alex Alekseyev, Vicky Zhou, Vikas Kakkar, Jarrod Helzer, Anurang Revri, Yair Bannett, Roxana Daneshjou, Jonathan Chen, Emily Alsentzer, Keith Morse, Nirmal Ravi, Nima Aghaeepour, Vanessa Kennedy, Akshay Chaudhari, Thomas Wang, Sanmi Koyejo, Matthew P. Lungren, Eric Horvitz, Percy Liang, Mike Pfeffer, Nigam H. Shah

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-06-02)

---

## 💡 一句话要点

**提出MedHELM框架以全面评估医疗任务中的大型语言模型表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗任务` `评估框架` `临床实践` `性能比较` `基准套件` `临床决策支持` `人工智能`

## 📋 核心要点

1. 现有的LLM评估方法未能充分反映真实临床实践的复杂性，导致评估结果的局限性。
2. MedHELM框架通过建立临床医生验证的分类法和综合基准套件，提供了更全面的LLM评估方法。
3. 实验结果显示，先进的推理模型在多个任务中表现优异，且LLM评审团的评估方法与临床医生的评分一致性较高。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在医疗执照考试中取得了近乎完美的分数，但这些评估并未充分反映真实临床实践的复杂性和多样性。本文介绍了MedHELM，一个可扩展的评估框架，旨在评估LLM在医疗任务中的表现，主要贡献包括：首先，开发了一个经过临床医生验证的分类法，涵盖5个类别、22个子类别和121个任务；其次，构建了一个包含35个基准的综合基准套件，全面覆盖分类法中的所有类别和子类别；最后，采用改进的评估方法（使用LLM评审团）对9个前沿LLM进行了系统比较，并进行了成本-性能分析。研究结果显示，先进推理模型表现优异，且Claude 3.5 Sonnet在较低计算成本下取得了可比的结果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在医疗任务评估中的不足，尤其是缺乏对真实临床场景的全面反映。现有方法往往只关注模型在标准化考试中的表现，未能考虑实际应用中的复杂性和多样性。

**核心思路**：MedHELM框架的核心思路是通过建立一个经过临床医生验证的分类法和全面的基准套件，来系统性地评估LLM在医疗任务中的表现。这种设计旨在确保评估的全面性和针对性，从而更好地反映模型在实际临床环境中的应用能力。

**技术框架**：MedHELM框架包括三个主要模块：1）分类法开发，涵盖5个类别和121个任务；2）基准套件构建，包含35个基准以全面覆盖分类法；3）评估方法，采用LLM评审团进行系统比较和成本-性能分析。

**关键创新**：MedHELM的关键创新在于其分类法和基准套件的系统性构建，以及使用LLM评审团进行评估的方法。这与传统的单一考试评估方法本质上不同，提供了更为全面和真实的评估视角。

**关键设计**：在设计过程中，研究团队与29位临床医生合作，确保分类法的有效性和实用性。基准套件中的任务涵盖了临床笔记生成、患者沟通与教育等多个方面，确保了评估的多样性和全面性。

## 📊 实验亮点

实验结果显示，9个前沿LLM在35个基准上的表现存在显著差异，其中DeepSeek R1和o3-mini的胜率分别为66%和64%。Claude 3.5 Sonnet在较低的计算成本下实现了与顶级模型相当的性能，强调了任务特定评估的重要性。

## 🎯 应用场景

MedHELM框架的潜在应用领域包括医疗人工智能助手、临床决策支持系统以及医疗教育等。通过提供更真实的评估标准，该框架能够帮助开发更有效的医疗语言模型，提升临床工作效率和患者沟通质量，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> While large language models (LLMs) achieve near-perfect scores on medical licensing exams, these evaluations inadequately reflect the complexity and diversity of real-world clinical practice. We introduce MedHELM, an extensible evaluation framework for assessing LLM performance for medical tasks with three key contributions. First, a clinician-validated taxonomy spanning 5 categories, 22 subcategories, and 121 tasks developed with 29 clinicians. Second, a comprehensive benchmark suite comprising 35 benchmarks (17 existing, 18 newly formulated) providing complete coverage of all categories and subcategories in the taxonomy. Third, a systematic comparison of LLMs with improved evaluation methods (using an LLM-jury) and a cost-performance analysis. Evaluation of 9 frontier LLMs, using the 35 benchmarks, revealed significant performance variation. Advanced reasoning models (DeepSeek R1: 66% win-rate; o3-mini: 64% win-rate) demonstrated superior performance, though Claude 3.5 Sonnet achieved comparable results at 40% lower estimated computational cost. On a normalized accuracy scale (0-1), most models performed strongly in Clinical Note Generation (0.73-0.85) and Patient Communication & Education (0.78-0.83), moderately in Medical Research Assistance (0.65-0.75), and generally lower in Clinical Decision Support (0.56-0.72) and Administration & Workflow (0.53-0.63). Our LLM-jury evaluation method achieved good agreement with clinician ratings (ICC = 0.47), surpassing both average clinician-clinician agreement (ICC = 0.43) and automated baselines including ROUGE-L (0.36) and BERTScore-F1 (0.44). Claude 3.5 Sonnet achieved comparable performance to top models at lower estimated cost. These findings highlight the importance of real-world, task-specific evaluation for medical use of LLMs and provides an open source framework to enable this.


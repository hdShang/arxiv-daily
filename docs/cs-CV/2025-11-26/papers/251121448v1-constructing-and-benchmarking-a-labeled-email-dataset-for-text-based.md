---
layout: default
title: Constructing and Benchmarking: a Labeled Email Dataset for Text-Based Phishing and Spam Detection Framework
---

# Constructing and Benchmarking: a Labeled Email Dataset for Text-Based Phishing and Spam Detection Framework

**arXiv**: [2511.21448v1](https://arxiv.org/abs/2511.21448) | [PDF](https://arxiv.org/pdf/2511.21448.pdf)

**作者**: Rebeka Toth, Tamas Bisztray, Richard Dubniczky

---

## 💡 一句话要点

**提出带标注邮件数据集以改进基于文本的网络钓鱼和垃圾邮件检测框架**

**关键词**: `邮件数据集` `网络钓鱼检测` `垃圾邮件分类` `大语言模型评估` `情感标注` `动机分析`

## 📋 核心要点

1. 网络钓鱼和垃圾邮件是主要网络安全威胁，攻击者利用大语言模型生成欺骗性内容
2. 构建包含钓鱼、垃圾和合法邮件的标注数据集，区分人类和LLM生成内容
3. 评估LLM识别情感和动机线索的能力，并测试分类模型在重述邮件上的鲁棒性

## 📄 摘要（原文）

> Phishing and spam emails remain a major cybersecurity threat, with attackers increasingly leveraging Large Language Models (LLMs) to craft highly deceptive content. This study presents a comprehensive email dataset containing phishing, spam, and legitimate messages, explicitly distinguishing between human- and LLM-generated content. Each email is annotated with its category, emotional appeal (e.g., urgency, fear, authority), and underlying motivation (e.g., link-following, credential theft, financial fraud). We benchmark multiple LLMs on their ability to identify these emotional and motivational cues and select the most reliable model to annotate the full dataset. To evaluate classification robustness, emails were also rephrased using several LLMs while preserving meaning and intent. A state-of-the-art LLM was then assessed on its performance across both original and rephrased emails using expert-labeled ground truth. The results highlight strong phishing detection capabilities but reveal persistent challenges in distinguishing spam from legitimate emails. Our dataset and evaluation framework contribute to improving AI-assisted email security systems. To support open science, all code, templates, and resources are available on our project site.


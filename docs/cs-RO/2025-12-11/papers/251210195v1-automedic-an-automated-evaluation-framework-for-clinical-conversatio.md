---
layout: default
title: AutoMedic: An Automated Evaluation Framework for Clinical Conversational Agents with Medical Dataset Grounding
---

# AutoMedic: An Automated Evaluation Framework for Clinical Conversational Agents with Medical Dataset Grounding

**arXiv**: [2512.10195v1](https://arxiv.org/abs/2512.10195) | [PDF](https://arxiv.org/pdf/2512.10195.pdf)

**作者**: Gyutaek Oh, Sangjoon Park, Byung-Hoon Kim

---

## 💡 一句话要点

**提出AutoMedic框架以自动化评估临床对话代理，基于医疗数据集模拟多轮对话**

**关键词**: `临床对话代理` `自动化评估框架` `多代理模拟` `医疗数据集` `多轮对话评估` `CARE指标`

## 📋 核心要点

1. 核心问题：现有静态医疗问答基准难以评估LLM在动态交互临床对话中的表现，缺乏标准化方法
2. 方法要点：将静态QA数据集转化为虚拟患者档案，通过多代理模拟实现自动化多轮临床对话评估
3. 实验或效果：引入CARE多维度评估指标，经专家验证框架有效性，为医疗对话应用提供开发指南

## 📄 摘要（原文）

> Evaluating large language models (LLMs) has recently emerged as a critical issue for safe and trustworthy application of LLMs in the medical domain. Although a variety of static medical question-answering (QA) benchmarks have been proposed, many aspects remain underexplored, such as the effectiveness of LLMs in generating responses in dynamic, interactive clinical multi-turn conversation situations and the identification of multi-faceted evaluation strategies beyond simple accuracy. However, formally evaluating a dynamic, interactive clinical situation is hindered by its vast combinatorial space of possible patient states and interaction trajectories, making it difficult to standardize and quantitatively measure such scenarios. Here, we introduce AutoMedic, a multi-agent simulation framework that enables automated evaluation of LLMs as clinical conversational agents. AutoMedic transforms off-the-shelf static QA datasets into virtual patient profiles, enabling realistic and clinically grounded multi-turn clinical dialogues between LLM agents. The performance of various clinical conversational agents is then assessed based on our CARE metric, which provides a multi-faceted evaluation standard of clinical conversational accuracy, efficiency/strategy, empathy, and robustness. Our findings, validated by human experts, demonstrate the validity of AutoMedic as an automated evaluation framework for clinical conversational agents, offering practical guidelines for the effective development of LLMs in conversational medical applications.


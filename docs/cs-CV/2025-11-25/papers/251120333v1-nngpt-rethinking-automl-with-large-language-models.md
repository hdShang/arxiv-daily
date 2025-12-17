---
layout: default
title: NNGPT: Rethinking AutoML with Large Language Models
---

# NNGPT: Rethinking AutoML with Large Language Models

**arXiv**: [2511.20333v1](https://arxiv.org/abs/2511.20333) | [PDF](https://arxiv.org/pdf/2511.20333.pdf)

**作者**: Roman Kochnev, Waleed Khalid, Tolgay Atinc Uzun, Xi Zhang, Yashkumar Sanjaybhai Dhameliya, Furui Qin, Chandini Vysyaraju, Raghuvir Duvvuri, Avi Goyal, Dmitry Ignatov, Radu Timofte

---

## 💡 一句话要点

**提出NNGPT框架，将大语言模型转化为自改进AutoML引擎，用于计算机视觉神经网络开发。**

**关键词**: `自改进AI` `AutoML` `神经网络合成` `大语言模型应用` `计算机视觉` `超参数优化`

## 📋 核心要点

1. 核心问题：构建自改进AI系统是AI领域的根本挑战。
2. 方法要点：集成五个LLM管道，实现生成、评估和自改进的闭环系统。
3. 实验或效果：在LEMUR数据集上，HPO的RMSE为0.60，优于Optuna。

## 📄 摘要（原文）

> Building self-improving AI systems remains a fundamental challenge in the AI domain. We present NNGPT, an open-source framework that turns a large language model (LLM) into a self-improving AutoML engine for neural network development, primarily for computer vision. Unlike previous frameworks, NNGPT extends the dataset of neural networks by generating new models, enabling continuous fine-tuning of LLMs based on closed-loop system of generation, assessment, and self-improvement. It integrates within one unified workflow five synergistic LLM-based pipelines: zero-shot architecture synthesis, hyperparameter optimization (HPO), code-aware accuracy/early-stop prediction, retrieval-augmented synthesis of scope-closed PyTorch blocks (NN-RAG), and reinforcement learning. Built on the LEMUR dataset as an audited corpus with reproducible metrics, NNGPT emits from a single prompt and validates network architecture, preprocessing code, and hyperparameters, executes them end-to-end, and learns from result. The PyTorch adapter makes NNGPT framework-agnostic, enabling strong performance: NN-RAG achieves 73% executability on 1,289 targets, 3-shot prompting boosts accuracy on common datasets, and hash-based deduplication saves hundreds of runs. One-shot prediction matches search-based AutoML, reducing the need for numerous trials. HPO on LEMUR achieves RMSE 0.60, outperforming Optuna (0.64), while the code-aware predictor reaches RMSE 0.14 with Pearson r=0.78. The system has already generated over 5K validated models, proving NNGPT as an autonomous AutoML engine. Upon acceptance, the code, prompts, and checkpoints will be released for public access to enable reproducibility and facilitate community usage.

